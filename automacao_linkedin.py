import os
from google import genai
import requests

# 1. Configurações das Chaves
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
LINKEDIN_TOKEN = os.environ.get("LINKEDIN_ACCESS_TOKEN")

print("--- Verificação de Segurança ---")
if not GEMINI_KEY or not LINKEDIN_TOKEN:
    print("❌ Erro: Chaves faltando!")
    exit(1)

# Inicializa Gemini 2.0
client = genai.Client(api_key=GEMINI_KEY)

def get_my_urn():
    """Busca o ID (sub) do usuário usando o endpoint OpenID Connect (OIDC)"""
    url = "https://api.linkedin.com/v2/userinfo"
    headers = {"Authorization": f"Bearer {LINKEDIN_TOKEN}"}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        # O LinkedIn retorna o ID no campo 'sub' para tokens novos
        return res.json().get("sub")
    print(f"Erro ao buscar URN: {res.status_code} - {res.text}")
    return None

def carregar_proximo_arquivo():
    if not os.path.exists("post_index.txt"):
        with open("post_index.txt", "w") as f: f.write("0")
    
    with open("post_index.txt", "r") as f:
        index = int(f.read().strip())
    
    arquivos_md = sorted([os.path.join(r, f) for r, d, fs in os.walk(".") 
                         for f in fs if f.endswith(".md") and "README" not in f.upper() and ".github" not in r])
    
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
    # Montando o payload para post de texto
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

# Fluxo Principal
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
            response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
            texto_gerado = response.text
            
            status, response_text = postar_no_linkedin(my_urn, texto_gerado)
            if status == 201:
                print("🚀 POST PUBLICADO NO LINKEDIN!")
                with open("post_index.txt", "w") as f: f.write(str(idx_atual + 1))
            else:
                print(f"❌ Erro na postagem: {status} - {response_text}")
        except Exception as e:
            print(f"❌ Erro Gemini: {e}")
    else:
        print("📁 Nenhum arquivo .md encontrado.")
