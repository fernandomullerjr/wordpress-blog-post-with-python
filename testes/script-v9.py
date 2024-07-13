import requests
import json
from deep_translator import GoogleTranslator
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

source_url = os.getenv("SOURCE_URL")
base_url = os.getenv("BASE_URL")
source_language = os.getenv("SOURCE_LANGUAGE")
target_language = os.getenv("TARGET_LANGUAGE")
wp_app_username = os.getenv("WP_APP_USERNAME")
wp_app_password = os.getenv("WP_APP_PASSWORD")

def create_gutenberg_block(block_name, attributes, inner_blocks, content):
    block = {
        "blockName": block_name,
        "attrs": attributes,
        "innerBlocks": inner_blocks,
        "innerHTML": content
    }
    return block

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

    # Analisa o conteúdo do post usando BeautifulSoup
    soup = BeautifulSoup(content_translation_text, 'html.parser')

    # Cria os blocos de conteúdo do Gutenberg
    content_blocks = []

    # Título
    content_blocks.append(create_gutenberg_block("core/heading", {"level": 1}, [], title_translation_text))

    # Parágrafos
    for paragraph in soup.find_all("p"):
        content_blocks.append(create_gutenberg_block("core/paragraph", {}, [], str(paragraph)))

    # Imagens
    for img in soup.find_all("img"):
        content_blocks.append(create_gutenberg_block("core/image", {"url": img["src"]}, [], ""))

    # Listas
    for ul in soup.find_all("ul"):
        list_items = []
        for li in ul.find_all("li"):
            list_items.append(create_gutenberg_block("core/list-item", {}, [], str(li)))
        content_blocks.append(create_gutenberg_block("core/list", {}, list_items, ""))

    # Títulos (h2, h3, etc.)
    for heading in soup.find_all(["h2", "h3", "h4", "h5", "h6"]):
        level = int(heading.name[1])
        content_blocks.append(create_gutenberg_block("core/heading", {"level": level}, [], str(heading)))

    # Tabelas
    for table in soup.find_all("table"):
        table_rows = []
        for tr in table.find_all("tr"):
            table_cells = []
            for td in tr.find_all("td"):
                table_cells.append(create_gutenberg_block("core/table-cell", {}, [], str(td)))
            table_rows.append(create_gutenberg_block("core/table-row", {}, table_cells, ""))
        content_blocks.append(create_gutenberg_block("core/table", {}, table_rows, ""))

    # Separadores
    for hr in soup.find_all("hr"):
        content_blocks.append(create_gutenberg_block("core/separator", {}, [], ""))

    # Citações
    for blockquote in soup.find_all("blockquote"):
        content_blocks.append(create_gutenberg_block("core/quote", {}, [], str(blockquote)))

    # Código
    for pre in soup.find_all("pre"):
        content_blocks.append(create_gutenberg_block("core/code", {}, [], str(pre)))

    # Tabela de Conteúdo
    toc_content = ""
    for toc_item in soup.find_all("a", {"class": "toc-link"}):
        toc_content += f"- [{toc_item.text}]({toc_item['href']})\n"
    if toc_content:
        content_blocks.append(create_gutenberg_block("core/paragraph", {}, [], toc_content))

    WP_url = wpBaseURL + "/wp-json/wp/v2/posts"

    auth = HTTPBasicAuth(wp_app_username, wp_app_password)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "status": postStatus,
        "title": title_translation_text,
        "content": json.dumps(content_blocks)
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
