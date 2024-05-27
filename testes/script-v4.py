import requests
import json
from deep_translator import GoogleTranslator
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

source_url = os.getenv("SOURCE_URL")
base_url = os.getenv("BASE_URL")
source_language = os.getenv("SOURCE_LANGUAGE")
target_language = os.getenv("TARGET_LANGUAGE")
wp_app_username = os.getenv("WP_APP_USERNAME")
wp_app_password = os.getenv("WP_APP_PASSWORD")

def post_creator(sourceURL, wpBaseURL, sourceLang, targetLang, postStatus):
    response_API = requests.get(sourceURL)
    
    if response_API.status_code != 200:
        print(f"Erro ao acessar a URL: {response_API.status_code}")
        return

    data = response_API.json()

    # Adiciona um print para mostrar o conteúdo do post obtido
    print("Conteúdo do post obtido:")
    print(json.dumps(data, indent=4, ensure_ascii=False))

    get_article_title = data['title']['rendered']
    get_article_content = data['content']['rendered']

    translator = GoogleTranslator(source=sourceLang, target=targetLang)

    title_translation_text = translator.translate(get_article_title)

    # Função para dividir o texto em pedaços menores que 4500 caracteres
    def split_text(text, max_length):
        parts = []
        while len(text) > max_length:
            split_index = text[:max_length].rfind(' ')
            if split_index == -1:
                split_index = max_length
            parts.append(text[:split_index])
            text = text[split_index:]
        parts.append(text)
        return parts

    # Divide o conteúdo do artigo em partes menores que 4500 caracteres
    content_parts = split_text(get_article_content, 4500)
    
    # Traduz cada parte
    translated_parts = [translator.translate(part) for part in content_parts]
    
    # Junta as partes traduzidas de volta em um único texto
    content_translation_text = ''.join(translated_parts)

    WP_url = wpBaseURL + "/wp-json/wp/v2/posts"

    auth = HTTPBasicAuth(wp_app_username, wp_app_password)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({ 
        "status": postStatus,
        "title": title_translation_text,
        "content": content_translation_text
    })

    response = requests.post(
        WP_url,
        data=payload,
        headers=headers,
        auth=auth
    )

    if response.status_code == 201:
        print("Post publicado com sucesso!")
    else:
        print(f"Erro ao publicar o post: {response.status_code}")
        print(response.json())

post_creator(source_url, base_url, source_language, target_language, "publish")
