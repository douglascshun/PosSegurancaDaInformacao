import os
import requests
import json
import google.generativeai as genai  # Biblioteca estável

# 1. CAPTURA AS CHAVES DO GITHUB ACTIONS
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
LINKEDIN_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")

print("--- Verificação de Segurança ---")
if not GEMINI_KEY or not LINKEDIN_TOKEN:
    print(f"❌ Erro: Chaves faltando! Gemini: {'OK' if GEMINI_KEY else 'Vazia'}, LinkedIn: {'OK' if LINKEDIN_TOKEN else 'Vazia'}")
    exit(1)

# 2. INICIALIZA O GEMINI (Método Robusto)
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def get_my_urn():
    """Busca o ID (sub) do usuário usando o endpoint OpenID Connect (OIDC)"""
    url = "https://api.linkedin.com/v2/userinfo"
    headers = {"Authorization": f"Bearer {LINKEDIN_TOKEN}"}
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.json().get("sub")
        print(f"Erro ao buscar URN: {res.status_code} - {res.text}")
    except Exception as e:
        print(f"Erro de conexão ao buscar URN: {e}")
    return None

def carregar_proximo_arquivo():
    if not os.path.exists("post_index.txt"):
        with open("post_index.txt", "w") as f: f.write("0")
    
    with open("post_index.txt", "r") as f:
        conteudo_index = f.read().strip()
        index = int(conteudo_index) if conteudo_index else 0
    
    arquivos_md = sorted([
        os.path.join(r, f) for r, d, fs in os.walk(".") 
        for f in fs if f.endswith(".md") and "README" not in f.upper() and ".github" not in r
    ])
    
    if not arquivos_md:
        return None, 0
    
    if index >= len(arquivos_md):
        index = 0  
        
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
    res = requests.post(url, headers=headers, json=payload)
    return res.status_code, res.text

# --- Fluxo Principal ---
my_urn = get_my_urn()
if my_urn:
    print(f"✅ URN obtida com sucesso: {my_urn}")
    arquivo_da_vez, idx_atual = carregar_proximo_arquivo()
    
    if arquivo_da_vez:
        print(f"📖 Lendo arquivo: {arquivo_da_vez}")
        with open(arquivo_da_vez, "r", encoding="utf-8") as f:
            conteudo = f.read()
        
        prompt = f"Crie um post para LinkedIn sobre este tema de Segurança da Informação: {conteudo}. Use emojis e hashtags."
        
        try:
            # 3. GERAÇÃO DE CONTEÚDO (Sintaxe da biblioteca estável)
            response = model.generate_content(prompt)
            texto_gerado = response.text
            
            print(f"🤖 Conteúdo gerado pela IA com sucesso!")
            
            status, response_text = postar_no_linkedin(my_urn, texto_gerado)
            if status == 201:
                print("🚀 POST PUBLICADO NO LINKEDIN!")
                with open("post_index.txt", "w") as f: f.write(str(idx_atual + 1))
            else:
                print(f"❌ Erro na postagem LinkedIn: {status} - {response_text}")
        except Exception as e:
            print(f"❌ Erro ao gerar conteúdo com Gemini: {e}")
    else:
        print("📁 Nenhum arquivo .md encontrado para postagem.")
else:
    print("❌ Não foi possível obter a URN do perfil.")
