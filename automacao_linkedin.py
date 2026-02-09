import os
import google.generativeai as genai
import requests
import json

# 1. Configurações das Chaves
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
LINKEDIN_TOKEN = os.environ.get("LINKEDIN_ACCESS_TOKEN")

print("--- Verificação de Segurança ---")
if not GEMINI_KEY:
    print("❌ Erro: Chave GEMINI_API_KEY não encontrada!")
if not LINKEDIN_TOKEN:
    print("❌ Erro: Chave LINKEDIN_ACCESS_TOKEN não encontrada!")

if GEMINI_KEY and LINKEDIN_TOKEN:
    print("✅ Chaves carregadas com sucesso!")
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel('gemini-pro')
else:
    exit(1) # Para a execução se não houver chaves

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
    
    arquivos_md = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".md") and "README" not in file.upper() and ".github" not in root:
                arquivos_md.append(os.path.join(root, file))
    
    arquivos_md.sort()
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
    print(f"Processando: {arquivo_da_vez}")
    
    with open(arquivo_da_vez, "r", encoding="utf-8") as f:
        conteudo = f.read()
    
    prompt = f"Atue como especialista em Segurança da Informação. Crie um post educativo para LinkedIn com emojis e hashtags baseado nisto: {conteudo}"
    
    try:
        response = model.generate_content(prompt)
        status = postar_no_linkedin(my_id, response.text)
        if status == 201:
            print("✅ Post publicado!")
            with open("post_index.txt", "w") as f: f.write(str(idx_atual + 1))
        else:
            print(f"❌ Erro LinkedIn: {status}")
    except Exception as e:
        print(f"❌ Erro IA: {e}")
