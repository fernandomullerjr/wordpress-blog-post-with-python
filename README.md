# wordpress-blog-post-with-python

Script que efetua a coleta de um post do Wordpress, traduz e efetua a publicação do post traduzido.

## Índice

- [Instalação](#instalacao)
- [Uso](#uso)
- [Observações](#observacoes)
- [Versões](#versoes)

## Instalação

### Bibliotecas

Instruções sobre como instalar e configurar o ambiente necessário para o projeto.

Primeiro, instalar os pacotes das bibliotecas que serão utilizadas:

```bash
pip3 install requests
pip3 install python-dotenv
pip3 install deep-translator
```

### Wordpress - APP Password

Precisamos ir ao painel do nosso site WordPress e criar uma nova senha do aplicativo. Usaremos isso para construir nossa autenticação básica ao enviar postagens para nosso site. 
Se você nunca fez isso antes, você pode verificar a documentação oficial do WordPress <https://make.wordpress.org/core/2020/11/05/application-passwords-integration-guide/> sobre como fazer isso.


## Uso

Como eu criei um ambiente virtual, dentro de um container Docker usando o Ubuntu como base, é necessário:

1. Iniciar o container Docker.
2. Conectar no container.
3. Carregar o ambiente virtual do Python.
4. Executar o script em Python.

Seguem os comandos utilizados:

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

## Versões

Seguem as versões utilizadas do Python e bibliotecas:

````bash
(ambiente-virtual-novo) root@1c297bab36f0:/# pip3 list | egrep 'deep|requests|dot'
deep-translator    1.11.4
python-dotenv      1.0.1
requests           2.31.0
(ambiente-virtual-novo) root@1c297bab36f0:/#
(ambiente-virtual-novo) root@1c297bab36f0:/# python3 --version
Python 3.12.3
(ambiente-virtual-novo) root@1c297bab36f0:/#

````