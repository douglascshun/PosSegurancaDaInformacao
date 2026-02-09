import os
import requests
from google import genai
from google.genai import types

# 1. CAPTURA AS CHAVES
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
LINKEDIN_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")

# 2. INICIALIZA O CLIENTE FORÇANDO A VERSÃO V1 (ESTÁVEL)
# Isso evita o erro 404 da v1beta que você recebeu
client = genai.Client(
    api_key=GEMINI_KEY,
    http_options=types.HttpOptions(api_version='v1')
)

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
        print(f"📖 Lendo: {arquivo}")
        with open(arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()
        
        try:
            # 3. GERAÇÃO USANDO O SDK NOVO
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=f"Crie um post de LinkedIn sobre: {conteudo}"
            )
            
            if response.text:
                res_post = postar_no_linkedin(my_urn, response.text)
                if res_post.status_code == 201:
                    print("🚀 SUCESSO!")
                    with open("post_index.txt", "w") as f: f.write(str(idx + 1))
                else:
                    print(f"❌ Erro LinkedIn: {res_post.status_code}")
        except Exception as e:
            print(f"❌ Erro Gemini: {e}")
