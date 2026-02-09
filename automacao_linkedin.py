import os
import google.generativeai as genai
import requests
import json

# 1. Configurações das Chaves (Lendo do cofre do GitHub Actions)
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
LINKEDIN_TOKEN = os.environ.get("LINKEDIN_ACCESS_TOKEN")

# Configura a IA
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')

def get_my_urn():
    """Descobre o seu ID do LinkedIn automaticamente"""
    url = "https://api.linkedin.com/v2/me"
    headers = {"Authorization": f"Bearer {LINKEDIN_TOKEN}"}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        return res.json().get("id")
    else:
        print(f"Erro ao buscar URN: {res.text}")
        return None

def carregar_proximo_arquivo():
    """Localiza o próximo .md da fila com base no índice salvo"""
    if not os.path.exists("post_index.txt"):
        with open("post_index.txt", "w") as f: f.write("0")
        
    with open("post_index.txt", "r") as f:
        index = int(f.read().strip())
    
    arquivos_md = []
    # Varre as pastas do repositório
    for root, dirs, files in os.walk("."):
        for file in files:
            # Filtra apenas arquivos de aula úteis
            if file.endswith(".md") and "README" not in file.upper() and ".github" not in root:
                arquivos_md.append(os.path.join(root, file))
    
    # Ordena alfabeticamente/numericamente
    arquivos_md.sort()
    
    # Se chegarmos ao fim da lista, reinicia do primeiro arquivo
    if index >= len(arquivos_md):
        print("Fim da lista atingido. Reiniciando do primeiro arquivo.")
        index = 0
        
    return arquivos_md[index], index

def postar_no_linkedin(urn, texto):
    """Envia o texto formatado para a API do LinkedIn"""
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

# --- PROCESSO PRINCIPAL ---
print("Iniciando processo de postagem automatizada...")

my_id = get_my_urn()
if my_id:
    arquivo_da_vez, idx_atual = carregar_proximo_arquivo()
    print(f"Arquivo selecionado: {arquivo_da_vez}")
    
    with open(arquivo_da_vez, "r", encoding="utf-8") as f:
        conteudo_estudo = f.read()
    
    # IA cria o conteúdo
    print("Solicitando à IA para criar o post...")
    prompt = (
        "Atue como um especialista em Segurança da Informação. "
        "Crie um post para o LinkedIn baseado nestas notas de estudo. "
        "Use uma linguagem clara, emojis e hashtags. "
        "O post deve ser educativo e direto. Máximo 2800 caracteres. "
        f"Notas: {conteudo_estudo}"
    )
    
    try:
        response = model.generate_content(prompt)
        texto_post = response.text
        
        # Publicação
        status = postar_no_linkedin(my_id, texto_post)
        
        if status == 201:
            print(f"✅ Sucesso! Postado no LinkedIn.")
            # Salva o progresso para amanhã
            with open("post_index.txt", "w") as f:
                f.write(str(idx_atual + 1))
        else:
            print(f"❌ Erro na API do LinkedIn. Status: {status}")
    except Exception as e:
        print(f"❌ Erro ao gerar conteúdo com a IA: {e}")
else:
    print("❌ Não foi possível obter o seu ID do LinkedIn. Verifique o Token.")
