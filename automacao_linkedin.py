import os
import requests
import google.generativeai as genai

# 1. CAPTURA AS CHAVES
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
LINKEDIN_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")

print("--- Verificação de Segurança ---")

# 2. INICIALIZAÇÃO ROBUSTA
genai.configure(api_key=GEMINI_KEY)
# Usando o modelo sem sufixos, que é o mais resiliente no SDK estável
model = genai.GenerativeModel('gemini-1.5-flash')

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
    if not os.path.exists("post_index.txt"):
        with open("post_index.txt", "w") as f: f.write("0")
    with open("post_index.txt", "r") as f:
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
    res = requests.post(url, headers=headers, json=payload)
    return res.status_code, res.text

# --- Fluxo Principal ---
my_urn = get_my_urn()
if my_urn:
    print(f"✅ URN obtida com sucesso: {my_urn}")
    arquivo, idx = carregar_proximo_arquivo()
    
    if arquivo:
        print(f"📖 Lendo: {arquivo}")
        with open(arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()
        
        prompt = f"Escreva um post curto para LinkedIn sobre: {conteudo}. Use emojis e hashtags."
        
        try:
            # A mágica está aqui: o SDK antigo gerencia melhor o fallback de DNS
            response = model.generate_content(prompt)
            texto_gerado = response.text
            
            status, res_text = postar_no_linkedin(my_urn, texto_gerado)
            if status == 201:
                print("🚀 POST PUBLICADO!")
                with open("post_index.txt", "w") as f: f.write(str(idx + 1))
            else:
                print(f"❌ Erro LinkedIn: {status}")
        except Exception as e:
            print(f"❌ Erro Gemini: {e}")
