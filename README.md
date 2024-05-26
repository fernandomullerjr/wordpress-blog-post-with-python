# wordpress-blog-post-with-python

Script que efetua a coleta de um post do Wordpress, traduz e efetua a publicação do post traduzido.

## Índice

- [Instalação](#instalacao)
- [Uso](#uso)
- [Observações](#observacoes)

## Instalação

Instruções sobre como instalar e configurar o ambiente necessário para o projeto.

```bash
pip3 install requests
pip3 install python-dotenv
pip3 install deep-translator
```

## Uso

```bash
docker start ubuntu
docker container exec -ti ubuntu bash
source /teste/ambiente-virtual-novo/bin/activate
python3 script.py
```


## Observações

### Porque a biblioteca deep-translator ao invés da biblioteca googletrans?

Foram encontrados erros durante os testes, erro "AttributeError: 'NoneType' object has no attribute 'group'", que geralmente ocorre quando a biblioteca googletrans não consegue obter o token de autenticação necessário para a tradução. Isso pode ser devido a mudanças na API do Google Translate, problemas temporários com o serviço ou a versão da biblioteca.

Para resolver isso, foi utilizada uma biblioteca alternativa: deep-translator, que também oferece suporte para tradução com o Google Translate.

Aqui está um exemplo de como usar a biblioteca deep-translator:

```bash
pip3 install deep-translator
```

Em seguida, atualize o script para usar deep-translator:

~~~~python
import requests
import json
from deep_translator import GoogleTranslator
~~~~