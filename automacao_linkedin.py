import os
import requests
from google import genai

# 1. CONFIGURAÇÃO DE CHAVES
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
LINKEDIN_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")

# 2. INICIALIZAÇÃO DO CLIENTE (PADRÃO 2026)
client = genai.Client(api_key=GEMINI_KEY)

def get_my_urn():
    url = "https://api.linkedin.com/v2/userinfo"
    headers = {"Authorization": f"Bearer {LINKEDIN_TOKEN}"}
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.json().get("sub")
    except: pass
    return None

def carregar_proximo_arquivo():
    index_file = "post_index.txt"
    if not os.path.exists(index_file):
        with open(index_file, "w") as f: f.write("0")
    with open(index_file, "r") as f:
        index = int(f.read().strip() or 0)
    
    arquivos_md = sorted([
        os.path.join(r, f) for r, d, fs in os.walk(".") 
        for f in fs if f.endswith(".md") and "README" not in f.upper() and ".github" not in r
    ])
    
    if not arquivos_md: return None, 0
    if index >= len(arquivos_md): index = 0
    return arquivos_md[index], index

def postar_no_linkedin(urn, texto):
    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {LINKEDIN_TOKEN}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }
    payload = {
        "author": f"urn:li:person:{urn}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": texto},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }
    return requests.post(url, headers=headers, json=payload)

# --- Fluxo Principal ---
my_urn = get_my_urn()
if my_urn:
    arquivo, idx = carregar_proximo_arquivo()
    if arquivo:
        print(f"📖 Lendo arquivo: {arquivo}")
        with open(arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()
        
        try:
            # 3. SOLICITAÇÃO AO GEMINI
            response = client.models.generate_content(
                model="gemini-3-flash-preview", 
                contents=(
                    f"Atue como um Especialista em Marketing de Conteúdo e Segurança da Informação, principalmente Red Team. "
                    f"Converta o conteúdo abaixo em um post para LinkedIn.\n\n"
                    f"CONTEÚDO BASE: {conteudo}\n\n"
                    "REGRAS CRÍTICAS:\n"
                    "1. RESPONDA APENAS COM O TEXTO FINAL DO POST.\n"
                    "2. NÃO inclua introduções como 'Aqui está o post' ou 'Claro'.\n"
                    "3. NÃO inclua aspas no início ou no fim.\n"
                    "4. Use HOOK, Bullet Points, Tom profissional/direto, CTA e 3 Hashtags.\n"
                    "5. Máximo 1300 caracteres.\n"
                    "6. NÃO USE EMOJIS." 
                )
            )
            
            if response.text:
                # --- PROCESSO DE LIMPEZA ---
                post_final = response.text.strip()

                # Remove negrito extra que o MD às vezes coloca no post inteiro
                if post_final.startswith("**") and post_final.endswith("**"):
                    post_final = post_final[2:-2] # Remove 2 caracteres de cada lado
                
                # Remove aspas extras
                if post_final.startswith('"') and post_final.endswith('"'):
                    post_final = post_final[1:-1]
                
                # Remove blocos de código markdown
                if post_final.startswith("```"):
                    linhas = post_final.split("\n")
                    post_final = "\n".join(linhas[1:-1]) if len(linhas) > 2 else post_final

                # Remove frases de introdução (Case Insensitive)
                intros_indesejadas = ["Aqui está", "Com certeza", "Segue a proposta", "Claro, aqui", "Com certeza!", "Aqui vai"]
                for intro in intros_indesejadas:
                    if post_final.lower().startswith(intro.lower()):
                        partes = post_final.split("\n", 1)
                        if len(partes) > 1:
                            post_final = partes[1].strip()

                # --- ENVIO PARA LINKEDIN ---
                res_post = postar_no_linkedin(my_urn, post_final)
                
                if res_post.status_code == 201:
                    print("🚀 Post publicado com sucesso!")
                    with open("post_index.txt", "w") as f: f.write(str(idx + 1))
                else:
                    print(f"❌ Erro LinkedIn ({res_post.status_code}): {res_post.text}")

        except Exception as e:
            print(f"❌ Erro Gemini: {e}")
        else:
            print("❌ Não foi possível obter a URN do LinkedIn. Verifique o TOKEN.")
