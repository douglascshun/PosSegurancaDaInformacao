import os
from google import genai
import requests
import json

# 1. Configurações das Chaves
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
LINKEDIN_TOKEN = os.environ.get("LINKEDIN_ACCESS_TOKEN")

print("--- Verificação de Segurança ---")
if not GEMINI_KEY or not LINKEDIN_TOKEN:
    print(f"❌ Erro: Chaves faltando! Gemini: {'OK' if GEMINI_KEY else 'FALTA'}, LinkedIn: {'OK' if LINKEDIN_TOKEN else 'FALTA'}")
    exit(1)

print("✅ Chaves detectadas no ambiente!")

# Configuração do novo Cliente Google GenAI
client = genai.Client(api_key=GEMINI_KEY)

def get_my_urn():
    url = "https://api.linkedin.com/v2/me"
    headers = {"Authorization": f"Bearer {LINKEDIN_TOKEN}"}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        return res.json().get("id")
    print(f"Erro ao buscar URN: {res.text}")
    return None

def carregar_proximo_arquivo():
    if not os.path.exists("post_index.txt"):
        with open("post_index.txt", "w") as f: f.write("0")
    
    with open("post_index.txt", "r") as f:
        index = int(f.read().strip())
    
    arquivos_md = sorted([os.path.join(r, f) for r, d, fs in os.walk(".") 
                         for f in fs if f.endswith(".md") and "README" not in f.upper() and ".github" not in r])
    
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
    return res.status_code

# Fluxo Principal
my_id = get_my_urn()
if my_id:
    arquivo_da_vez, idx_atual = carregar_proximo_arquivo()
    if not arquivo_da_vez:
        print("❌ Nenhum arquivo .md encontrado para postar.")
        exit(0)

    print(f"Processando: {arquivo_da_vez}")
    with open(arquivo_da_vez, "r", encoding="utf-8") as f:
        conteudo = f.read()
    
    prompt = f"Crie um post educativo para LinkedIn com emojis e hashtags baseado nisto: {conteudo}"
    
    try:
        # Chamada usando a nova biblioteca
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        status = postar_no_linkedin(my_id, response.text)
        
        if status == 201:
            print("✅ Post publicado com sucesso!")
            with open("post_index.txt", "w") as f: f.write(str(idx_atual + 1))
        else:
            print(f"❌ Erro LinkedIn (Status {status})")
    except Exception as e:
        print(f"❌ Erro na IA: {e}")
