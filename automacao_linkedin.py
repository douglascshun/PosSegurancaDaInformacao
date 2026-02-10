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
            # 3. SOLICITAÇÃO AO GEMINI (MODELO 3 FLASH PREVIEW)
            response = client.models.generate_content(
                model="gemini-3-flash-preview", 
                contents=(
    f"Atue como um Especialista em Marketing de Conteúdo e LinkedIn Creator, e Segurança da Informação "
    f"Seu objetivo é transformar o conteúdo técnico abaixo em um post de alto impacto para o LinkedIn. "
    f"\n\nCONTEÚDO BASE: {conteudo} \n\n"
    "DIRETRIZES DE FORMATAÇÃO:"
    "\n1. HOOK: Comece com uma frase de impacto (gancho) que gere curiosidade ou ataque uma dor comum."
    "\n2. CORPO: Use bullet points para facilitar a leitura (escaneabilidade)."
    "\n3. TOM: Profissional, porém leve e autêntico (evite termos corporativos excessivamente genéricos)."
    "\n4. CTA: Termine com uma pergunta para incentivar comentários."
    "\n5. EMOJIS: Use moderadamente para pontuar os tópicos."
    "\n6. HASHTAGS: Adicione 3 hashtags relevantes ao final."
    "\n\nRestrição: O texto deve ter no máximo 1300 caracteres."
    )
)
            
            if response.text:
                res_post = postar_no_linkedin(my_urn, response.text)
                if res_post.status_code == 201:
                    print("🚀 Post publicado com sucesso!")
                    with open("post_index.txt", "w") as f: f.write(str(idx + 1))
                else:
                    print(f"❌ Erro LinkedIn ({res_post.status_code}): {res_post.text}")
        except Exception as e:
            print(f"❌ Erro Gemini: {e}")
else:
    print("❌ Não foi possível obter a URN do LinkedIn. Verifique o TOKEN.")
