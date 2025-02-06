





# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## COMANDOS

git status
git add .
git commit -m "Wordpress with Python."
git push
git status

docker start ubuntu
docker container exec -ti ubuntu bash

cd teste/
    2  ls
    3  python3 script.py
    4  ls -lhasp
    5  pip3 install virtualenv
    6  apt install python3-venv
    7  pwd
    8  mkdir ambiente-virtual-novo
    9  python3 -m venv /teste/ambiente-virtual-novo
   10  source /teste/ambiente-virtual-novo/bin/activate
   11  pip3 install requests
   12  pip3 install googletrans
   13  date
   14  pip3 install python-dotenv
   15  ls -lhasp
   16  ls -lhasp ambiente-virtual-novo/
   17  python3 script.py
   18  history


python3 -m venv /teste/ambiente-virtual-novo
source /teste/ambiente-virtual-novo/bin/activate

python3 script.py


git add .
git commit -m "Wordpress with Python."
git push



# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## versão validada

/home/fernando/cursos/python/wordpress-blog-post-with-python/testes/script-v4.py
v1.0.0
traduz, mas traz no editor classico

- Testando
cria o post ok
porém:
1. O "Table of Contents" vem como editor clássico no post traduzido.
2. Capa é perdida.
3. HREFLANG, idioma vem igual ao idioma do post original, necessário ajustar lógica do script para ajustar o HREFLANG para o TARGET_LANGUAGE.
4. Paragrafos vem em editor clássico, precisam vir em Blocos.



# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## TUTORIAL


<https://www.freecodecamp.org/news/how-to-generate-wordpress-posts-automatically/>



# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## Application Passwords

Before that, we need to go to the dashboard of our WordPress website and create a new application password. We'll use it to build our basic authentication when pushing posts to our website. 

If you've never done it before, you can check WordPress official documentation <https://make.wordpress.org/core/2020/11/05/application-passwords-integration-guide/> on how to do it. 
Once you'll create it, you'll see something like this:

fernando-pale-senha-11-05-2024

Sua nova senha para fernando-pale-senha-11-05-2024 é: 





# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## Time to Code

Let's start checking out our code from the libraries we need. We'll use the googletrans library to translate our content with Google translate APIs. So, from the command line, I move to my project directory and type:

pip install googletrans

- ERRO

~~~~BASH
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ pip install googletrans
Collecting googletrans
  Downloading https://files.pythonhosted.org/packages/71/3a/3b19effdd4c03958b90f40fe01c93de6d5280e03843cc5adf6956bfc9512/googletrans-3.0.0.tar.gz
Collecting httpx==0.13.3 (from googletrans)
  Could not find a version that satisfies the requirement httpx==0.13.3 (from googletrans) (from versions: )
No matching distribution found for httpx==0.13.3 (from googletrans)
You have new mail in /var/mail/fernando
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$

~~~~


- Usando pip3 funcionou:

~~~~bash

fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ pip3 install googletrans
Collecting googletrans
  Using cached https://files.pythonhosted.org/packages/71/3a/3b19effdd4c03958b90f40fe01c93de6d5280e03843cc5adf6956bfc9512/googletrans-3.0.0.tar.gz
Collecting httpx==0.13.3 (from googletrans)
  Downloading https://files.pythonhosted.org/packages/54/b4/698b284c6aed4d7c2b4fe3ba5df1fcf6093612423797e76fbb24890dd22f/httpx-0.13.3-py3-none-any.whl (55kB)
    100% |████████████████████████████████| 61kB 3.0MB/s
Requirement already satisfied: certifi in /usr/lib/python3/dist-packages (from httpx==0.13.3->googletrans) (2018.8.24)
Collecting hstspreload (from httpx==0.13.3->googletrans)
  Downloading https://files.pythonhosted.org/packages/39/fd/faadcac67dbeeb0c85faf64ce6481e88cfa1f60643f246d1326c13934466/hstspreload-2024.5.1-py3-none-any.whl (1.1MB)
    100% |████████████████████████████████| 1.2MB 2.2MB/s
Requirement already satisfied: idna==2.* in /usr/lib/python3/dist-packages (from httpx==0.13.3->googletrans) (2.6)
Collecting httpcore==0.9.* (from httpx==0.13.3->googletrans)
  Downloading https://files.pythonhosted.org/packages/dd/d5/e4ff9318693ac6101a2095e580908b591838c6f33df8d3ee8dd953ba96a8/httpcore-0.9.1-py3-none-any.whl (42kB)
    100% |████████████████████████████████| 51kB 22.7MB/s
Requirement already satisfied: chardet==3.* in /usr/lib/python3/dist-packages (from httpx==0.13.3->googletrans) (3.0.4)
Collecting rfc3986<2,>=1.3 (from httpx==0.13.3->googletrans)
  Downloading https://files.pythonhosted.org/packages/c4/e5/63ca2c4edf4e00657584608bee1001302bbf8c5f569340b78304f2f446cb/rfc3986-1.5.0-py2.py3-none-any.whl
Collecting sniffio (from httpx==0.13.3->googletrans)
  Downloading https://files.pythonhosted.org/packages/e9/44/75a9c9421471a6c4805dbf2356f7c181a29c1879239abab1ea2cc8f38b40/sniffio-1.3.1-py3-none-any.whl
Collecting h11<0.10,>=0.8 (from httpcore==0.9.*->httpx==0.13.3->googletrans)
  Downloading https://files.pythonhosted.org/packages/5a/fd/3dad730b0f95e78aeeb742f96fa7bbecbdd56a58e405d3da440d5bfb90c6/h11-0.9.0-py2.py3-none-any.whl (53kB)
    100% |████████████████████████████████| 61kB 21.1MB/s
Collecting h2==3.* (from httpcore==0.9.*->httpx==0.13.3->googletrans)
  Downloading https://files.pythonhosted.org/packages/25/de/da019bcc539eeab02f6d45836f23858ac467f584bfec7a526ef200242afe/h2-3.2.0-py2.py3-none-any.whl (65kB)
    100% |████████████████████████████████| 71kB 21.4MB/s
Collecting hyperframe<6,>=5.2.0 (from h2==3.*->httpcore==0.9.*->httpx==0.13.3->googletrans)
  Downloading https://files.pythonhosted.org/packages/19/0c/bf88182bcb5dce3094e2f3e4fe20db28a9928cb7bd5b08024030e4b140db/hyperframe-5.2.0-py2.py3-none-any.whl
Collecting hpack<4,>=3.0 (from h2==3.*->httpcore==0.9.*->httpx==0.13.3->googletrans)
  Downloading https://files.pythonhosted.org/packages/8a/cc/e53517f4a1e13f74776ca93271caef378dadec14d71c61c949d759d3db69/hpack-3.0.0-py2.py3-none-any.whl
Building wheels for collected packages: googletrans
  Running setup.py bdist_wheel for googletrans ... done
  Stored in directory: /home/fernando/.cache/pip/wheels/28/1a/a7/eaf4d7a3417a0c65796c547cff4deb6d79c7d14c2abd29273e
Successfully built googletrans
Installing collected packages: hstspreload, h11, hyperframe, hpack, h2, sniffio, httpcore, rfc3986, httpx, googletrans
Successfully installed googletrans-3.0.0 h11-0.9.0 h2-3.2.0 hpack-3.0.0 hstspreload-2024.5.1 httpcore-0.9.1 httpx-0.13.3 hyperframe-5.2.0 rfc3986-1.5.0 sniffio-1.3.1
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$

~~~~

You could encounter this error when you run the script:

AttributeError: 'NoneType' object has no attribute 'group'

If you see this message error, you should install this version:

pip install googletrans==4.0.0-rc1

I found it on this StackOverflow article. If you want to know more about it, just have a look!
<https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group>








# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## How to Get the Content Translated

Once we install googletrans, we define a new function and call it "post_creator":

def post_creator(sourceURL, wpBaseURL, sourceLang, targetLang, postStatus):

We pass this function five arguments:

    sourceURL: the URL of the website you get content from
    wpBaseURL: the URL of your new website where you want to import translated content
    sourceLang: the original language of the content
    targetLang: the language you want your content to be translated into
    postStatus: the status of your WordPress post: for example "draft", "published", and so on.







# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## Variáveis


<https://www.twilio.com/en-us/blog/environment-variables-python>


pip install python-dotenv
pip3 install python-dotenv

~~~~bash

fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ pip3 install python-dotenv
Collecting python-dotenv
  Downloading https://files.pythonhosted.org/packages/64/62/f19d1e9023aacb47241de3ab5a5d5fedf32c78a71a9e365bb2153378c141/python_dotenv-0.21.1-py3-none-any.whl
Installing collected packages: python-dotenv
Successfully installed python-dotenv-0.21.1
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$

~~~~


- Adicionando no código python:

~~~~python
from dotenv import load_dotenv
load_dotenv()
~~~~


- Material sobre o dotenv
<https://pypi.org/project/python-dotenv/>



- Como acessar as variáveis:
<https://dev.to/emma_donery/python-dotenv-keep-your-secrets-safe-4ocn>

exemplo


Access the Environment Variables

~~~~python
from dotenv import load_dotenv
import os #provides ways to access the Operating System and allows us to read the environment variables

load_dotenv()

my_id = os.getenv("ID")
my_secret_key = os.getenv("SECRET_KEY")

def myEnvironment():
    print(f'My id is: {my_id}.')
    print(f'My secret key is: {my_secret_key}.')

if __name__ == "__main__":
    myEnvironment()
~~~~




<https://py-googletrans.readthedocs.io/en/latest/>





# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## Checks

<https://blog.finxter.com/how-to-publish-a-wordpress-post-using-python/>
Enable the REST API in WordPress: WordPress has a REST API built in that you can use to interact with the site via Python. The REST API is enabled by default in WordPress 4.7 and later. You can check if it’s available by visiting http://your-site-url/wp-json/.

- Validando:
<https://palegreen-hornet-335449.hostingersite.com/wp-json/>

~~~~json
name	"palegreen-hornet-335449.hostingersite.com"
description	""
url	"https://palegreen-hornet-335449.hostingersite.com"
home	"https://palegreen-hornet-335449.hostingersite.com"
gmt_offset	-3
timezone_string	"America/Sao_Paulo"
namespaces	[…]
authentication	{…}
routes	{…}
site_logo	0
site_icon	0
site_icon_url	""
_links	{…}
~~~~



python -m pip install requests
python3 -m pip3 install requests
python3 -m pip install requests

pip3 install requests


fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ pip3 install requests
Requirement already satisfied: requests in /usr/lib/python3/dist-packages (2.21.0)
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$




# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
##  TESTES

- Testando v1,

~~~~python
import requests
import json
import random
from googletrans import Translator
from requests.auth import HTTPBasicAuth
import os #provides ways to access the Operating System and allows us to read the environment variables
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.
source_url = os.getenv("SOURCE_URL")
base_url = os.getenv("BASE_URL")
source_language = os.getenv("SOURCE_LANGUAGE")
target_language = os.getenv("TARGET_LANGUAGE")
wp_app_username = os.getenv("WP_APP_USERNAME")
wp_app_password = os.getenv("WP_APP_PASSWORD")

def post_creator(sourceURL, wpBaseURL, sourceLang, targetLang, postStatus):
    response_API = requests.get(sourceURL)
    data = response_API.text
    parse_json = json.loads(data)
    get_article_title = parse_json['title']
    get_article_content = parse_json['body']
#    image_list = ["1689","1594","1612"]

    translator = Translator()

    title_translation = translator.translate(get_article_title, src=sourceLang, dest=targetLang)
    title_translation_text = title_translation.text 

    content_translation = translator.translate(get_article_content, src=sourceLang, dest=targetLang)
    content_translation_text = content_translation.text 

#    random_image_list = random.choice(image_list)

    WP_url = wpBaseURL + "/wp-json/wp/v2/posts"

    auth = HTTPBasicAuth({wp_app_username}, {wp_app_password})

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps({ 
        "status":postStatus,
        "title": title_translation_text,
        "content": content_translation_text,
#        "featured_media": random_image_list
    })

    response = requests.request(
    "POST",
    WP_url,
    data=payload,
    headers=headers,
    auth=auth
    )

    print(response)
#    print(random_image_list)


post_creator({source_url}, {base_url}, {source_language}, {target_language}, "publish")
~~~~





fernando@debian10x64:~$ python3 /home/fernando/cursos/python/wordpress-blog-post-with-python/script.py
Traceback (most recent call last):
  File "/home/fernando/cursos/python/wordpress-blog-post-with-python/script.py", line 1, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
fernando@debian10x64:~$



fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ python3 script.py
Traceback (most recent call last):
  File "script.py", line 1, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$





fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ python -m pip show requests
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ python3 -m pip show requests
/usr/local/bin/python3: No module named pip
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$




fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ pip install requests
Collecting requests
  Downloading https://files.pythonhosted.org/packages/2d/61/08076519c80041bc0ffa1a8af0cbd3bf3e2b62af10435d269a9d0f40564d/requests-2.27.1-py2.py3-none-any.whl (63kB)
    100% |████████████████████████████████| 71kB 3.1MB/s
Collecting urllib3<1.27,>=1.21.1 (from requests)
  Downloading https://files.pythonhosted.org/packages/b0/53/aa91e163dcfd1e5b82d8a890ecf13314e3e149c05270cc644581f77f17fd/urllib3-1.26.18-py2.py3-none-any.whl (143kB)
    100% |████████████████████████████████| 153kB 4.8MB/s
Collecting certifi>=2017.4.17 (from requests)
  Downloading https://files.pythonhosted.org/packages/37/45/946c02767aabb873146011e665728b680884cd8fe70dde973c640e45b775/certifi-2021.10.8-py2.py3-none-any.whl (149kB)
    100% |████████████████████████████████| 153kB 11.1MB/s
Collecting idna<3,>=2.5; python_version < "3" (from requests)
  Downloading https://files.pythonhosted.org/packages/a2/38/928ddce2273eaa564f6f50de919327bf3a00f091b5baba8dfa9460f3a8a8/idna-2.10-py2.py3-none-any.whl (58kB)
    100% |████████████████████████████████| 61kB 16.6MB/s
Collecting chardet<5,>=3.0.2; python_version < "3" (from requests)
  Downloading https://files.pythonhosted.org/packages/19/c7/fa589626997dd07bd87d9269342ccb74b1720384a4d739a1872bd84fbe68/chardet-4.0.0-py2.py3-none-any.whl (178kB)
    100% |████████████████████████████████| 184kB 9.5MB/s
Installing collected packages: urllib3, certifi, idna, chardet, requests
Successfully installed certifi-2021.10.8 chardet-4.0.0 idna-2.10 requests-2.27.1 urllib3-1.26.18
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$


fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ pip3 install requests
Requirement already satisfied: requests in /usr/lib/python3/dist-packages (2.21.0)
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$



sudo apt-get install python3-requests

Reading package lists... Done
Building dependency tree
Reading state information... Done
python3-requests is already the newest version (2.21.0-1+deb10u1).
python3-requests set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 49 not upgraded.




pip freeze | grep requests

pip3 freeze | grep requests


fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ pip3 freeze | grep requests
requests==2.21.0
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$

fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ pip3 uninstall requests
Not uninstalling requests at /usr/lib/python3/dist-packages, outside environment /usr
Can't uninstall 'requests'. No files were found to uninstall.
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$


sudo apt remove python3-requests

fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ sudo apt remove python3-requests
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages were automatically installed and are no longer required:
  gir1.2-dazzle-1.0 gir1.2-grilo-0.3 gir1.2-mediaart-2.0 hyphen-en-us libreoffice-help-common libreoffice-help-en-us mythes-en-us node-normalize.css python3-certifi python3-cups python3-debian python3-debianbts python3-httplib2 python3-idna python3-pysimplesoap
  python3-smbc python3-urllib3
Use 'sudo apt autoremove' to remove them.
The following packages will be REMOVED:
  chrome-gnome-shell gnome gnome-core gnome-music python3-cupshelpers python3-reportbug python3-requests reportbug system-config-printer-common system-config-printer-udev task-gnome-desktop
0 upgraded, 0 newly installed, 11 to remove and 49 not upgraded.
After this operation, 8,253 kB disk space will be freed.
Do you want to continue? [Y/n] Y
(Reading database ... 183276 files and directories currently installed.)
Removing chrome-gnome-shell (10.1-5) ...
Removing gnome (1:3.30+1) ...
Removing task-gnome-desktop (3.53) ...
Removing gnome-core (1:3.30+1) ...
Removing gnome-music (3.30.2-1) ...
Removing system-config-printer-udev (1.5.11-4) ...
Removing system-config-printer-common (1.5.11-4) ...
Removing python3-cupshelpers (1.5.11-4) ...
Removing reportbug (7.5.3~deb10u2) ...
Removing python3-reportbug (7.5.3~deb10u2) ...
Removing python3-requests (2.21.0-1+deb10u1) ...
Processing triggers for mime-support (3.62) ...
Processing triggers for hicolor-icon-theme (0.17-2) ...
Processing triggers for gnome-menus (3.31.4-3) ...
Processing triggers for libglib2.0-0:amd64 (2.58.3-2+deb10u5) ...
Processing triggers for man-db (2.8.5-2+deb10u1) ...
Processing triggers for desktop-file-utils (0.23-4) ...
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$

fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ pip3 freeze | grep requests
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$






pip3 install requests

~~~~bash
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ pip3 install requests
Collecting requests
  Downloading https://files.pythonhosted.org/packages/70/8e/0e2d847013cb52cd35b38c009bb167a1a26b2ce6cd6965bf26b47bc0bf44/requests-2.31.0-py3-none-any.whl (62kB)
    100% |████████████████████████████████| 71kB 3.2MB/s
Collecting charset-normalizer<4,>=2 (from requests)
  Downloading https://files.pythonhosted.org/packages/28/76/e6222113b83e3622caa4bb41032d0b1bf785250607392e1b778aca0b8a7d/charset_normalizer-3.3.2-py3-none-any.whl (48kB)
    100% |████████████████████████████████| 51kB 9.9MB/s
Requirement already satisfied: certifi>=2017.4.17 in /usr/lib/python3/dist-packages (from requests) (2018.8.24)
Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/lib/python3/dist-packages (from requests) (1.24.1)
Requirement already satisfied: idna<4,>=2.5 in /usr/lib/python3/dist-packages (from requests) (2.6)
Installing collected packages: charset-normalizer, requests
Successfully installed charset-normalizer-3.3.2 requests-2.31.0
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ date
Sat 11 May 2024 02:24:22 PM -03
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$
~~~~


fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ python3 script.py
Traceback (most recent call last):
  File "script.py", line 1, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$



fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ which python3
/usr/local/bin/python3
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$




Requirement already satisfied: requests in /home/fernando/.local/lib/python3.7/site-packages (2.31.0)
Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/lib/python3/dist-packages (from requests) (1.24.1)
Requirement already satisfied: charset-normalizer<4,>=2 in /home/fernando/.local/lib/python3.7/site-packages (from requests) (3.3.2)
Requirement already satisfied: idna<4,>=2.5 in /usr/lib/python3/dist-packages (from requests) (2.6)
Requirement already satisfied: certifi>=2017.4.17 in /usr/lib/python3/dist-packages (from requests) (2018.8.24)
fernando@debian10x64:/usr/local/bin$ sudo pip3 install requests
[sudo] password for fernando:
Collecting requests
  Downloading https://files.pythonhosted.org/packages/70/8e/0e2d847013cb52cd35b38c009bb167a1a26b2ce6cd6965bf26b47bc0bf44/requests-2.31.0-py3-none-any.whl (62kB)
    100% |████████████████████████████████| 71kB 3.3MB/s
Requirement already satisfied: idna<4,>=2.5 in /usr/lib/python3/dist-packages (from requests) (2.6)
Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/lib/python3/dist-packages (from requests) (1.24.1)
Requirement already satisfied: certifi>=2017.4.17 in /usr/lib/python3/dist-packages (from requests) (2018.8.24)
Collecting charset-normalizer<4,>=2 (from requests)
  Downloading https://files.pythonhosted.org/packages/28/76/e6222113b83e3622caa4bb41032d0b1bf785250607392e1b778aca0b8a7d/charset_normalizer-3.3.2-py3-none-any.whl (48kB)
    100% |████████████████████████████████| 51kB 9.6MB/s
Installing collected packages: charset-normalizer, requests
Successfully installed charset-normalizer-3.3.2 requests-2.31.0
fernando@debian10x64:/usr/local/bin$ date
Sat 11 May 2024 02:28:14 PM -03
fernando@debian10x64:/usr/local/bin$




fernando@debian10x64:/usr/local/bin$ pip3 freeze | grep requests
requests==2.31.0
fernando@debian10x64:/usr/local/bin$ python3 /home/fernando/cursos/python/wordpress-blog-post-with-python/script.py
Traceback (most recent call last):
  File "/home/fernando/cursos/python/wordpress-blog-post-with-python/script.py", line 1, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
fernando@debian10x64:/usr/local/bin$



~~~~bash
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ python3
.git/      script.py
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ python3 script.py
Traceback (most recent call last):
  File "script.py", line 1, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$
~~~~



~~~~bash
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ pip3 install requests
Requirement already satisfied: requests in /usr/lib/python3/dist-packages (2.21.0)
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$
~~~~








- Testes utilizando o Python 2 mesmo:

~~~~bash

  949  pip install requests
  950  pip install googletrans
  951  pip install httpx
  952  pip install http
  953  pip install googletrans
  954  pip install googletrans==2.3.0
  955  python script.py
  956  pip install dotenv
  957  python script.py
  958  pip install python-dotenv
  959  python script.py
  960  history
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ python script.py
Traceback (most recent call last):
  File "script.py", line 66, in <module>
    post_creator({source_url}, {base_url}, {source_language}, {target_language}, "publish")
  File "script.py", line 21, in post_creator
    response_API = requests.get(sourceURL)
  File "/home/fernando/.local/lib/python2.7/site-packages/requests/api.py", line 75, in get
    return request('get', url, params=params, **kwargs)
  File "/home/fernando/.local/lib/python2.7/site-packages/requests/api.py", line 61, in request
    return session.request(method=method, url=url, **kwargs)
  File "/home/fernando/.local/lib/python2.7/site-packages/requests/sessions.py", line 529, in request
    resp = self.send(prep, **send_kwargs)
  File "/home/fernando/.local/lib/python2.7/site-packages/requests/sessions.py", line 639, in send
    adapter = self.get_adapter(url=request.url)
  File "/home/fernando/.local/lib/python2.7/site-packages/requests/sessions.py", line 732, in get_adapter
    raise InvalidSchema("No connection adapters were found for {!r}".format(url))
requests.exceptions.InvalidSchema: No connection adapters were found for u"set(['https://palegreen-hornet-335449.hostingersite.com/ola-mundo/'])"
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$

~~~~




# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## PENDENTE

- Subir VM com Ubuntu 24 + Python3:
instalar python mais recente
configurar venv??
instalar as dependencias do projeto via pip3
efetuar teste do script

- Tentar instalar dependencias no Python3 do Debian-10.
configurar venv??











## Dia 12/05/2024

- Testar com docker
docker container run -d python:3.13.0b1-bullseye


docker run -d ubuntu

<https://linuxconfig.org/how-to-start-a-docker-container-as-daemon-process>
docker run -d --name ubuntu ubuntu /bin/bash -c 'while true; do sleep 30; done'
docker container exec -ti ubuntu bash

<https://phoenixnap.com/kb/how-to-install-python-3-ubuntu>
apt update
apt install python3

<https://phoenixnap.com/kb/how-to-install-pip-on-ubuntu>
apt update
apt install python3-pip
pip3 --version


<https://github.com/pypa/pipx>
pipx
apt update
apt install pipx
pipx ensurepath
pipx ensurepath --global # optional to allow pipx actions with --global argument



~~~~bash
root@1c297bab36f0:/teste#
root@1c297bab36f0:/teste# vi script.py
root@1c297bab36f0:/teste#
root@1c297bab36f0:/teste#
root@1c297bab36f0:/teste#
root@1c297bab36f0:/teste# ls -lhasp
total 12K
4.0K drwxr-xr-x 2 root root 4.0K May 12 10:37 ./
4.0K drwxr-xr-x 1 root root 4.0K May 12 10:35 ../
4.0K -rw-r--r-- 1 root root 2.1K May 12 10:37 script.py
root@1c297bab36f0:/teste#
root@1c297bab36f0:/teste#
root@1c297bab36f0:/teste#
root@1c297bab36f0:/teste# vi .env
root@1c297bab36f0:/teste# pipx list
nothing has been installed with pipx 😴
root@1c297bab36f0:/teste#
root@1c297bab36f0:/teste#
root@1c297bab36f0:/teste#
root@1c297bab36f0:/teste# pipx install googletrans
  installed package googletrans 3.0.0, installed using Python 3.12.3
  These apps are now globally available
    - translate
⚠️  Note: '/root/.local/bin' is not on your PATH environment variable. These apps will not be globally accessible until your PATH is updated. Run `pipx ensurepath` to automatically add it, or manually modify your PATH in your shell's config file (i.e. ~/.bashrc).
done! ✨ 🌟 ✨
root@1c297bab36f0:/teste#


root@1c297bab36f0:/teste#
root@1c297bab36f0:/teste# pipx install requests
Note: Dependent package 'charset-normalizer' contains 1 apps
  - normalizer

No apps associated with package requests. Try again with '--include-deps' to include apps of dependent packages, which are listed above. If you are attempting to install a library, pipx should not be used. Consider using pip or a similar tool instead.
root@1c297bab36f0:/teste# pipx ensurepath
/root/.local/bin has been been added to PATH, but you need to open a new terminal or re-login for this PATH change to take effect.

You will need to open a new terminal or re-login for the PATH changes to take effect.

Otherwise pipx is ready to go! ✨ 🌟 ✨
root@1c297bab36f0:/teste#
root@1c297bab36f0:/teste#
root@1c297bab36f0:/teste#
root@1c297bab36f0:/teste#
root@1c297bab36f0:/teste# pipx install requests --include-deps
  installed package requests 2.31.0, installed using Python 3.12.3
  These apps are now globally available
    - normalizer
⚠️  Note: '/root/.local/bin' is not on your PATH environment variable. These apps will not be globally accessible until your PATH is updated. Run `pipx ensurepath` to automatically add it, or manually modify your PATH in your shell's config file (i.e. ~/.bashrc).
done! ✨ 🌟 ✨
root@1c297bab36f0:/teste# pipx ensurepath
/root/.local/bin has been been added to PATH, but you need to open a new terminal or re-login for this PATH change to take effect.

You will need to open a new terminal or re-login for the PATH changes to take effect.

Otherwise pipx is ready to go! ✨ 🌟 ✨
root@1c297bab36f0:/teste#

pipx install dotenv


root@1c297bab36f0:/teste# pipx install dotenv
Fatal error from pip prevented installation. Full pip output in file:
    /root/.local/state/pipx/log/cmd_2024-05-12_10.44.01_pip_errors.log

pip seemed to fail to build package:
    dotenv

Some possibly relevant errors from pip install:
    error: subprocess-exited-with-error
    error: invalid command 'dist_info'
    error: metadata-generation-failed

Error installing dotenv.
root@1c297bab36f0:/teste#


pipx install python-dotenv


root@1c297bab36f0:/teste# pipx install python-dotenv
  installed package python-dotenv 1.0.1, installed using Python 3.12.3
  These apps are now globally available
    - dotenv
⚠️  Note: '/root/.local/bin' is not on your PATH environment variable. These apps will not be globally accessible until your PATH is updated. Run `pipx ensurepath` to automatically add it, or manually modify your PATH in your shell's config file (i.e. ~/.bashrc).
done! ✨ 🌟 ✨
root@1c297bab36f0:/teste#
root@1c297bab36f0:/teste#
root@1c297bab36f0:/teste# pipx ensurepath
/root/.local/bin has been been added to PATH, but you need to open a new terminal or re-login for this PATH change to take effect.

You will need to open a new terminal or re-login for the PATH changes to take effect.

Otherwise pipx is ready to go! ✨ 🌟 ✨
root@1c297bab36f0:/teste#


docker container exec -ti ubuntu bash


root@1c297bab36f0:/teste# ls
script.py
root@1c297bab36f0:/teste# python3 script.py
Traceback (most recent call last):
  File "/teste/script.py", line 4, in <module>
    from googletrans import Translator
ModuleNotFoundError: No module named 'googletrans'
root@1c297bab36f0:/teste#
~~~~




- Verificando que os pacotes não existem no pip ou pip3

~~~~bash
root@1c297bab36f0:/teste# pip3 list
WARNING: Skipping /usr/lib/python3.12/dist-packages/argcomplete-3.1.4.dist-info due to invalid metadata entry 'name'
Package      Version
------------ ----------
argcomplete  3.1.4
certifi      2023.11.17
chardet      5.2.0
click        8.1.6
colorama     0.4.6
idna         3.6
packaging    24.0
pip          24.0
pipx         1.4.3
platformdirs 4.2.0
psutil       5.9.8
requests     2.31.0
setuptools   68.1.2
urllib3      2.0.7
userpath     1.9.1
wheel        0.42.0
root@1c297bab36f0:/teste# pip3 install googletrans
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.

    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.

    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
root@1c297bab36f0:/teste#

~~~~





<https://www.baeldung.com/linux/pip-fix-externally-managed-environment-error>

apt install python3-venv
mkdir ambiente-virtual-novo
python3 -m venv /teste/ambiente-virtual-novo
source /teste/ambiente-virtual-novo/bin/activate

~~~~bash
root@1c297bab36f0:/teste#
root@1c297bab36f0:/teste# apt install python3-venv
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
python3-venv is already the newest version (3.12.3-0ubuntu1).
python3-venv set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
root@1c297bab36f0:/teste#

root@1c297bab36f0:/teste#
root@1c297bab36f0:/teste# pwd
/teste
root@1c297bab36f0:/teste# mkdir ambiente-virtual-novo
root@1c297bab36f0:/teste# python3 -m venv /teste/ambiente-virtual-novo
root@1c297bab36f0:/teste#
root@1c297bab36f0:/teste#
root@1c297bab36f0:/teste# source /teste/ambiente-virtual-novo/bin/activate
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
~~~~



- Instalando dependencias no ambiente virtual:

~~~~bash
(ambiente-virtual-novo) root@1c297bab36f0:/teste# pip3 install requests
Collecting requests
  Using cached requests-2.31.0-py3-none-any.whl.metadata (4.6 kB)
Collecting charset-normalizer<4,>=2 (from requests)
  Using cached charset_normalizer-3.3.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (33 kB)
Collecting idna<4,>=2.5 (from requests)
  Using cached idna-3.7-py3-none-any.whl.metadata (9.9 kB)
Collecting urllib3<3,>=1.21.1 (from requests)
  Using cached urllib3-2.2.1-py3-none-any.whl.metadata (6.4 kB)
Collecting certifi>=2017.4.17 (from requests)
  Using cached certifi-2024.2.2-py3-none-any.whl.metadata (2.2 kB)
Using cached requests-2.31.0-py3-none-any.whl (62 kB)
Using cached certifi-2024.2.2-py3-none-any.whl (163 kB)
Using cached charset_normalizer-3.3.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (141 kB)
Using cached idna-3.7-py3-none-any.whl (66 kB)
Using cached urllib3-2.2.1-py3-none-any.whl (121 kB)
Installing collected packages: urllib3, idna, charset-normalizer, certifi, requests
Successfully installed certifi-2024.2.2 charset-normalizer-3.3.2 idna-3.7 requests-2.31.0 urllib3-2.2.1
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste# pip3 install googletrans
Collecting googletrans
  Using cached googletrans-3.0.0-py3-none-any.whl
Collecting httpx==0.13.3 (from googletrans)
  Using cached httpx-0.13.3-py3-none-any.whl.metadata (25 kB)
Requirement already satisfied: certifi in ./ambiente-virtual-novo/lib/python3.12/site-packages (from httpx==0.13.3->googletrans) (2024.2.2)
Collecting hstspreload (from httpx==0.13.3->googletrans)
  Using cached hstspreload-2024.5.1-py3-none-any.whl.metadata (2.1 kB)
Collecting sniffio (from httpx==0.13.3->googletrans)
  Using cached sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
Collecting chardet==3.* (from httpx==0.13.3->googletrans)
  Using cached chardet-3.0.4-py2.py3-none-any.whl.metadata (3.2 kB)
Collecting idna==2.* (from httpx==0.13.3->googletrans)
  Using cached idna-2.10-py2.py3-none-any.whl.metadata (9.1 kB)
Collecting rfc3986<2,>=1.3 (from httpx==0.13.3->googletrans)
  Using cached rfc3986-1.5.0-py2.py3-none-any.whl.metadata (6.5 kB)
Collecting httpcore==0.9.* (from httpx==0.13.3->googletrans)
  Using cached httpcore-0.9.1-py3-none-any.whl.metadata (4.6 kB)
Collecting h11<0.10,>=0.8 (from httpcore==0.9.*->httpx==0.13.3->googletrans)
  Using cached h11-0.9.0-py2.py3-none-any.whl.metadata (8.1 kB)
Collecting h2==3.* (from httpcore==0.9.*->httpx==0.13.3->googletrans)
  Using cached h2-3.2.0-py2.py3-none-any.whl.metadata (32 kB)
Collecting hyperframe<6,>=5.2.0 (from h2==3.*->httpcore==0.9.*->httpx==0.13.3->googletrans)
  Using cached hyperframe-5.2.0-py2.py3-none-any.whl.metadata (7.2 kB)
Collecting hpack<4,>=3.0 (from h2==3.*->httpcore==0.9.*->httpx==0.13.3->googletrans)
  Using cached hpack-3.0.0-py2.py3-none-any.whl.metadata (7.0 kB)
Using cached httpx-0.13.3-py3-none-any.whl (55 kB)
Using cached chardet-3.0.4-py2.py3-none-any.whl (133 kB)
Using cached httpcore-0.9.1-py3-none-any.whl (42 kB)
Using cached idna-2.10-py2.py3-none-any.whl (58 kB)
Using cached sniffio-1.3.1-py3-none-any.whl (10 kB)
Using cached h2-3.2.0-py2.py3-none-any.whl (65 kB)
Using cached rfc3986-1.5.0-py2.py3-none-any.whl (31 kB)
Using cached hstspreload-2024.5.1-py3-none-any.whl (1.1 MB)
Using cached h11-0.9.0-py2.py3-none-any.whl (53 kB)
Using cached hpack-3.0.0-py2.py3-none-any.whl (38 kB)
Using cached hyperframe-5.2.0-py2.py3-none-any.whl (12 kB)
Installing collected packages: rfc3986, hyperframe, hpack, h11, chardet, sniffio, idna, hstspreload, h2, httpcore, httpx, googletrans
  Attempting uninstall: idna
    Found existing installation: idna 3.7
    Uninstalling idna-3.7:
      Successfully uninstalled idna-3.7
Successfully installed chardet-3.0.4 googletrans-3.0.0 h11-0.9.0 h2-3.2.0 hpack-3.0.0 hstspreload-2024.5.1 httpcore-0.9.1 httpx-0.13.3 hyperframe-5.2.0 idna-2.10 rfc3986-1.5.0 sniffio-1.3.1
(ambiente-virtual-novo) root@1c297bab36f0:/teste# date
Sun May 12 11:38:02 -03 2024
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste# pip3 install python-dotenv
Collecting python-dotenv
  Using cached python_dotenv-1.0.1-py3-none-any.whl.metadata (23 kB)
Using cached python_dotenv-1.0.1-py3-none-any.whl (19 kB)
Installing collected packages: python-dotenv
Successfully installed python-dotenv-1.0.1
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
~~~~



- Testando:

~~~~bash

(ambiente-virtual-novo) root@1c297bab36f0:/teste# python3 script.py
Traceback (most recent call last):
  File "/teste/script.py", line 66, in <module>
    post_creator({source_url}, {base_url}, {source_language}, {target_language}, "publish")
  File "/teste/script.py", line 21, in post_creator
    response_API = requests.get(sourceURL)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/teste/ambiente-virtual-novo/lib/python3.12/site-packages/requests/api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/teste/ambiente-virtual-novo/lib/python3.12/site-packages/requests/api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/teste/ambiente-virtual-novo/lib/python3.12/site-packages/requests/sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/teste/ambiente-virtual-novo/lib/python3.12/site-packages/requests/sessions.py", line 697, in send
    adapter = self.get_adapter(url=request.url)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/teste/ambiente-virtual-novo/lib/python3.12/site-packages/requests/sessions.py", line 794, in get_adapter
    raise InvalidSchema(f"No connection adapters were found for {url!r}")
requests.exceptions.InvalidSchema: No connection adapters were found for "{'https://palegreen-hornet-335449.hostingersite.com/ola-mundo/'}"
(ambiente-virtual-novo) root@1c297bab36f0:/teste#

~~~~




  File "/teste/ambiente-virtual-novo/lib/python3.12/site-packages/requests/sessions.py", line 794, in get_adapter
    raise InvalidSchema(f"No connection adapters were found for {url!r}")
requests.exceptions.InvalidSchema: No connection adapters were found for "{'https://palegreen-hornet-335449.hostingersite.com/ola-mundo/'}"






# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## COMANDOS

    1  cd teste/
    2  ls
    3  python3 script.py
    4  ls -lhasp
    5  pip3 install virtualenv
    6  apt install python3-venv
    7  pwd
    8  mkdir ambiente-virtual-novo
    9  python3 -m venv /teste/ambiente-virtual-novo
   10  source /teste/ambiente-virtual-novo/bin/activate
   11  pip3 install requests
   12  pip3 install googletrans
   13  date
   14  pip3 install python-dotenv
   15  ls -lhasp
   16  ls -lhasp ambiente-virtual-novo/
   17  python3 script.py
   18  history








# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## PENDENTE

- Tratar erro ao executar script.py:

  File "/teste/ambiente-virtual-novo/lib/python3.12/site-packages/requests/sessions.py", line 794, in get_adapter
    raise InvalidSchema(f"No connection adapters were found for {url!r}")
requests.exceptions.InvalidSchema: No connection adapters were found for "{'https://palegreen-hornet-335449.hostingersite.com/ola-mundo/'}"


- Fixar versões contidas no "requirements.txt"












- Tratar erro ao executar script.py:

~~~~bash
  File "/teste/ambiente-virtual-novo/lib/python3.12/site-packages/requests/sessions.py", line 794, in get_adapter
    raise InvalidSchema(f"No connection adapters were found for {url!r}")
requests.exceptions.InvalidSchema: No connection adapters were found for "{'https://palegreen-hornet-335449.hostingersite.com/ola-mundo/'}"
~~~~


 erro que você está enfrentando é "InvalidSchema: No connection adapters were found for {url!r}". Isso geralmente ocorre quando a URL passada para a função requests.get() não tem um esquema válido, como "http://" ou "https://".

Vou explicar como corrigir isso no seu script Python.

No seu script, você está passando as variáveis entre chaves {} quando chama a função post_creator(), o que não é necessário. Você já extraiu essas variáveis do ambiente com os.getenv(), então você deve passá-las diretamente para a função. Além disso, ao passar essas variáveis, não é necessário colocá-las entre chaves. O uso de chaves cria um conjunto, não uma variável individual. Aqui está como você deve chamar a função post_creator():

python

post_creator(source_url, base_url, source_language, target_language, "publish")

Além disso, você deve garantir que a variável source_url esteja corretamente definida no seu arquivo .env e inclua o esquema (por exemplo, "http://" ou "https://") na URL. Por exemplo:

arduino

SOURCE_URL=http://example.com/source

Depois de corrigir isso, seu script deverá funcionar corretamente. Certifique-se de que todas as outras variáveis do ambiente, como BASE_URL, SOURCE_LANGUAGE, TARGET_LANGUAGE, WP_APP_USERNAME e WP_APP_PASSWORD, estejam definidas corretamente no seu arquivo .env.




na linha "auth = HTTPBasicAuth({wp_app_username}, {wp_app_password})", estou usando corretamente as variáveis?

preciso utilizar {}?
ChatGPT

Não, na linha "auth = HTTPBasicAuth({wp_app_username}, {wp_app_password})", você não precisa usar as chaves {}. A função HTTPBasicAuth() espera que você passe as strings diretamente como argumentos, não dentro de conjuntos {}. Então, você deve passar wp_app_username e wp_app_password diretamente, sem as chaves.

Aqui está como você deve corrigir essa linha:

python

auth = HTTPBasicAuth(wp_app_username, wp_app_password)

Essa correção permitirá que a função HTTPBasicAuth() receba as strings corretas para autenticação básica no WordPress.




- Ajustando o código, v2:

~~~~python
import requests
import json
import random
from googletrans import Translator
from requests.auth import HTTPBasicAuth
import os #provides ways to access the Operating System and allows us to read the environment variables
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.
source_url = os.getenv("SOURCE_URL")
base_url = os.getenv("BASE_URL")
source_language = os.getenv("SOURCE_LANGUAGE")
target_language = os.getenv("TARGET_LANGUAGE")
wp_app_username = os.getenv("WP_APP_USERNAME")
wp_app_password = os.getenv("WP_APP_PASSWORD")

def post_creator(sourceURL, wpBaseURL, sourceLang, targetLang, postStatus):
    response_API = requests.get(sourceURL)
    data = response_API.text
    parse_json = json.loads(data)
    get_article_title = parse_json['title']
    get_article_content = parse_json['body']
#    image_list = ["1689","1594","1612"]

    translator = Translator()

    title_translation = translator.translate(get_article_title, src=sourceLang, dest=targetLang)
    title_translation_text = title_translation.text 

    content_translation = translator.translate(get_article_content, src=sourceLang, dest=targetLang)
    content_translation_text = content_translation.text 

#    random_image_list = random.choice(image_list)

    WP_url = wpBaseURL + "/wp-json/wp/v2/posts"

    auth = HTTPBasicAuth(wp_app_username, wp_app_password)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps({ 
        "status":postStatus,
        "title": title_translation_text,
        "content": content_translation_text,
#        "featured_media": random_image_list
    })

    response = requests.request(
    "POST",
    WP_url,
    data=payload,
    headers=headers,
    auth=auth
    )

    print(response)
#    print(random_image_list)


post_creator(source_url, base_url, source_language, target_language, "publish")
~~~~






- OK, resolvido o erro :
requests.exceptions.InvalidSchema: No connection adapters were found for "{'https://palegreen-hornet-335449.hostingersite.com/ola-mundo/'}"

- Novo erro:

~~~~bash

(ambiente-virtual-novo) root@1c297bab36f0:/teste# python3 script.py
Traceback (most recent call last):
  File "/teste/script.py", line 66, in <module>
    post_creator(source_url, base_url, source_language, target_language, "publish")
  File "/teste/script.py", line 23, in post_creator
    parse_json = json.loads(data)
                 ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste# date
Sun May 12 13:01:47 -03 2024
(ambiente-virtual-novo) root@1c297bab36f0:/teste#

~~~~




git add .
git commit -m "OK, RESOLVIDO O ERRO: requests.exceptions.InvalidSchema: No connection adapters were found for . NOVO ERRO, verificando: raise JSONDecodeError Expecting value  s, err.value from None"
git push











## GPT

O erro que você está enfrentando indica que há um problema ao decodificar o JSON retornado pela solicitação GET para sourceURL. O erro específico é json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0), o que sugere que a resposta não contém um JSON válido.

Existem algumas razões pelas quais isso pode estar acontecendo:

    Resposta vazia ou não JSON: A solicitação GET para sourceURL pode estar retornando uma resposta vazia ou em um formato diferente de JSON. Isso pode ocorrer, por exemplo, se o URL estiver incorreto ou se o servidor não estiver respondendo como esperado.

    Problemas de conexão ou autorização: Pode haver problemas de conexão com o URL especificado ou pode ser que o servidor requeira autenticação e as credenciais fornecidas não sejam válidas.

Para diagnosticar o problema:

    Certifique-se de que o URL em sourceURL esteja correto e que você possa acessá-lo manualmente em um navegador ou através de outras ferramentas de teste de API.

    Verifique se as credenciais de autenticação (wp_app_username e wp_app_password) estão corretas e se o servidor do WordPress está configurado para aceitá-las.

    Considere adicionar tratamento de erro ao seu código para lidar com possíveis problemas de rede ou resposta inválida, como uma resposta vazia. Isso pode ajudar a tornar o seu script mais robusto e fornecer informações mais úteis sobre o que está dando errado.



## GEMINI

The error "json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)" indicates that the json.loads function is unable to parse the content retrieved from sourceURL as valid JSON. Here are some potential causes and solutions:

1. The Response Might Not Be JSON:

    The URL you're fetching data from might not actually return JSON data. Verify the source's documentation or inspect the response using a tool like Postman or browser developer tools to confirm the content type (it should be application/json).
    If the source doesn't return JSON, you'll need to use a different parsing method appropriate for the actual data format (e.g., HTML parsing for HTML content).

2. Empty Response:

    If the source URL doesn't return any data or returns an error, response_API.text could be empty. Attempting to decode an empty string as JSON will lead to this error.
    Consider adding error handling to check the response status code before processing the content:

Python

response_API = requests.get(sourceURL)
if response_API.status_code == 200:
    data = response_API.text
    # ... rest of your code
else:
    print(f"Error fetching data: {response_API.status_code}")

Use o código com cuidado.

3. Malformed JSON:

    The response might contain invalid JSON formatting (e.g., missing quotes, extra commas). You can use online JSON validators to check for such issues.
    If you have control over the source, fix the JSON formatting to adhere to the standard.

Debugging Tips:

    Print the content of data (the response text) before attempting to decode it to see what you're actually working with.
    Try using a simpler test URL that returns valid JSON data to isolate if the issue is with the script or the source URL.

By addressing these potential causes, you should be able to resolve the JSON decoding error and proceed with processing the content successfully.






~~~~BASH


Traceback (most recent call last):
  File "/teste/script.py", line 66, in <module>
    post_creator(source_url, base_url, source_language, target_language, "publish")
  File "/teste/script.py", line 23, in post_creator
    parse_json = json.loads(data)
                 ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
~~~~




- Ajustando a variável:
SOURCE_URL="https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/posts/1"


- Teste

- ERRO:

~~~~BASH
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste# python3 script.py
Traceback (most recent call last):
  File "/teste/script.py", line 66, in <module>
    post_creator(source_url, base_url, source_language, target_language, "publish")
  File "/teste/script.py", line 25, in post_creator
    get_article_content = parse_json['body']
                          ~~~~~~~~~~^^^^^^^^
KeyError: 'body'
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
~~~~





# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## PENDENTE

- Tratar erro ao executar script.py. Erro pode estar relacionado a não formação do JSON ou autenticação junto ao Wordpress, verificar. Ver como obter JSON do post.
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

Usar o endpoint "https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/posts/" ou verificar o exato, estilo "https://jsonplaceholder.typicode.com/posts/5" , ou "https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/posts/1"

revisar dicas:
<https://amazonwebshark.com/using-python-aws-to-extract-wordpress-api-data/>

ver
<https://kinsta.com/blog/python-wordpress/>
<https://robingeuens.com/blog/python-wordpress-api/>
<https://medium.com/analytics-vidhya/wordpress-rest-api-with-python-f53a25827b1c>

- Adicionar try, exception, logs de erros.
- Fixar versões contidas no "requirements.txt", definir versões exatas.
- Criar Dockerfile e docker-compose, posteriormente.






# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## Dia 25/05/2024

docker start ubuntu
docker container exec -ti ubuntu bash

python3 -m venv /teste/ambiente-virtual-novo
source /teste/ambiente-virtual-novo/bin/activate

python3 script.py


- Teste, erro:

~~~~bash

(ambiente-virtual-novo) root@1c297bab36f0:/teste# python3 script.py
Traceback (most recent call last):
  File "/teste/script.py", line 66, in <module>
    post_creator(source_url, base_url, source_language, target_language, "publish")
  File "/teste/script.py", line 25, in post_creator
    get_article_content = parse_json['body']
                          ~~~~~~~~~~^^^^^^^^
KeyError: 'body'
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste# date
Sat May 25 21:45:59 -03 2024
(ambiente-virtual-novo) root@1c297bab36f0:/teste#

~~~~



- Atual
SOURCE_URL="https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/posts/1"



O erro KeyError: 'body' indica que a chave 'body' não está presente no dicionário parse_json que você está tentando acessar. Isso pode ocorrer se a resposta da API não contiver a chave esperada.

Para resolver esse problema, é importante adicionar verificações para garantir que a resposta da API contenha as chaves esperadas antes de tentar acessá-las. Além disso, pode ser útil imprimir a resposta da API para depuração. Vamos modificar o código para incluir essas verificações e também para imprimir a resposta da API caso ocorra um erro:

~~~~python
import requests
import json
import random
from googletrans import Translator
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.
source_url = os.getenv("SOURCE_URL")
base_url = os.getenv("BASE_URL")
source_language = os.getenv("SOURCE_LANGUAGE")
target_language = os.getenv("TARGET_LANGUAGE")
wp_app_username = os.getenv("WP_APP_USERNAME")
wp_app_password = os.getenv("WP_APP_PASSWORD")

def post_creator(sourceURL, wpBaseURL, sourceLang, targetLang, postStatus):
    response_API = requests.get(sourceURL)
    data = response_API.text
    
    try:
        parse_json = json.loads(data)
        get_article_title = parse_json['title']
        get_article_content = parse_json['body']
    except KeyError as e:
        print(f"KeyError: {e}")
        print(f"Response JSON: {parse_json}")
        return

    translator = Translator()

    title_translation = translator.translate(get_article_title, src=sourceLang, dest=targetLang)
    title_translation_text = title_translation.text 

    content_translation = translator.translate(get_article_content, src=sourceLang, dest=targetLang)
    content_translation_text = content_translation.text 

    WP_url = wpBaseURL + "/wp-json/wp/v2/posts"

    auth = HTTPBasicAuth(wp_app_username, wp_app_password)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({ 
        "status": postStatus,
        "title": title_translation_text,
        "content": content_translation_text,
    })

    response = requests.request(
        "POST",
        WP_url,
        data=payload,
        headers=headers,
        auth=auth
    )

    print(response)

post_creator(source_url, base_url, source_language, target_language, "publish")

~~~~





- Ajustando

- Teste

~~~~bash

(ambiente-virtual-novo) root@1c297bab36f0:/teste# vi script.py
(ambiente-virtual-novo) root@1c297bab36f0:/teste# python3 script.py
KeyError: 'body'
Response JSON: {'id': 1, 'date': '2024-05-11T12:14:35', 'date_gmt': '2024-05-11T15:14:35', 'guid': {'rendered': 'https://palegreen-hornet-335449.hostingersite.com/?p=1'}, 'modified': '2024-05-11T12:14:35', 'modified_gmt': '2024-05-11T15:14:35', 'slug': 'ola-mundo', 'status': 'publish', 'type': 'post', 'link': 'https://palegreen-hornet-335449.hostingersite.com/ola-mundo/', 'title': {'rendered': 'Olá, mundo!'}, 'content': {'rendered': '\n<p>Boas-vindas ao WordPress. Esse é o seu primeiro post. Edite-o ou exclua-o, e então comece a escrever!</p>\n', 'protected': False}, 'excerpt': {'rendered': '<p>Boas-vindas ao WordPress. Esse é o seu primeiro post. Edite-o ou exclua-o, e então comece a escrever!</p>\n', 'protected': False}, 'author': 1, 'featured_media': 0, 'comment_status': 'open', 'ping_status': 'open', 'sticky': False, 'template': '', 'format': 'standard', 'meta': {'site-sidebar-layout': 'default', 'site-content-layout': '', 'ast-site-content-layout': '', 'site-content-style': 'default', 'site-sidebar-style': 'default', 'ast-global-header-display': '', 'ast-banner-title-visibility': '', 'ast-main-header-display': '', 'ast-hfb-above-header-display': '', 'ast-hfb-below-header-display': '', 'ast-hfb-mobile-header-display': '', 'site-post-title': '', 'ast-breadcrumbs-content': '', 'ast-featured-img': '', 'footer-sml-layout': '', 'theme-transparent-header-meta': '', 'adv-header-id-meta': '', 'stick-header-meta': '', 'header-above-stick-meta': '', 'header-main-stick-meta': '', 'header-below-stick-meta': '', 'astra-migrate-meta-layouts': 'default', 'ast-page-background-enabled': 'default', 'ast-page-background-meta': {'desktop': {'background-color': 'var(--ast-global-color-4)', 'background-image': '', 'background-repeat': 'repeat', 'background-position': 'center center', 'background-size': 'auto', 'background-attachment': 'scroll', 'background-type': '', 'background-media': '', 'overlay-type': '', 'overlay-color': '', 'overlay-gradient': ''}, 'tablet': {'background-color': '', 'background-image': '', 'background-repeat': 'repeat', 'background-position': 'center center', 'background-size': 'auto', 'background-attachment': 'scroll', 'background-type': '', 'background-media': '', 'overlay-type': '', 'overlay-color': '', 'overlay-gradient': ''}, 'mobile': {'background-color': '', 'background-image': '', 'background-repeat': 'repeat', 'background-position': 'center center', 'background-size': 'auto', 'background-attachment': 'scroll', 'background-type': '', 'background-media': '', 'overlay-type': '', 'overlay-color': '', 'overlay-gradient': ''}}, 'ast-content-background-meta': {'desktop': {'background-color': 'var(--ast-global-color-5)', 'background-image': '', 'background-repeat': 'repeat', 'background-position': 'center center', 'background-size': 'auto', 'background-attachment': 'scroll', 'background-type': '', 'background-media': '', 'overlay-type': '', 'overlay-color': '', 'overlay-gradient': ''}, 'tablet': {'background-color': 'var(--ast-global-color-5)', 'background-image': '', 'background-repeat': 'repeat', 'background-position': 'center center', 'background-size': 'auto', 'background-attachment': 'scroll', 'background-type': '', 'background-media': '', 'overlay-type': '', 'overlay-color': '', 'overlay-gradient': ''}, 'mobile': {'background-color': 'var(--ast-global-color-5)', 'background-image': '', 'background-repeat': 'repeat', 'background-position': 'center center', 'background-size': 'auto', 'background-attachment': 'scroll', 'background-type': '', 'background-media': '', 'overlay-type': '', 'overlay-color': '', 'overlay-gradient': ''}}, 'footnotes': ''}, 'categories': [1], 'tags': [], 'aioseo_notices': [], '_links': {'self': [{'href': 'https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/posts/1'}], 'collection': [{'href': 'https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/posts'}], 'about': [{'href': 'https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/types/post'}], 'author': [{'embeddable': True, 'href': 'https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/users/1'}], 'replies': [{'embeddable': True, 'href': 'https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/comments?post=1'}], 'version-history': [{'count': 0, 'href': 'https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/posts/1/revisions'}], 'wp:attachment': [{'href': 'https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/media?parent=1'}], 'wp:term': [{'taxonomy': 'category', 'embeddable': True, 'href': 'https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/categories?post=1'}, {'taxonomy': 'post_tag', 'embeddable': True, 'href': 'https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/tags?post=1'}], 'curies': [{'name': 'wp', 'href': 'https://api.w.org/{rel}', 'templated': True}]}}
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste# date
Sat May 25 22:02:40 -03 2024
(ambiente-virtual-novo) root@1c297bab36f0:/teste#

~~~~





- Criando v2

Para criar um script Python que faça uma requisição a uma API do WordPress para obter um post, traduzir o título e o conteúdo do post do português para o inglês usando a biblioteca googletrans, e publicar o post traduzido de volta no WordPress, siga o exemplo abaixo. Esse código usa a biblioteca requests para fazer as requisições HTTP e a biblioteca googletrans para a tradução.

Primeiro, instale as bibliotecas necessárias se ainda não tiver feito isso:

sh

pip install requests googletrans-python python-dotenv

Em seguida, crie um arquivo .env no mesmo diretório do seu script Python para armazenar as variáveis de ambiente:

makefile

SOURCE_URL=https://seu-site.com/wp-json/wp/v2/posts/1
BASE_URL=https://seu-site.com
SOURCE_LANGUAGE=pt
TARGET_LANGUAGE=en
WP_APP_USERNAME=seu-usuario
WP_APP_PASSWORD=sua-senha

Agora, aqui está o script Python completo:

~~~~python

import requests
import json
from googletrans import Translator
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
    get_article_title = data['title']['rendered']
    get_article_content = data['content']['rendered']

    translator = Translator()

    title_translation = translator.translate(get_article_title, src=sourceLang, dest=targetLang)
    title_translation_text = title_translation.text 

    content_translation = translator.translate(get_article_content, src=sourceLang, dest=targetLang)
    content_translation_text = content_translation.text 

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
~~~~

Explicação do Código:

    Carregamento das Variáveis de Ambiente: Usa a biblioteca dotenv para carregar variáveis de ambiente do arquivo .env.
    Requisição do Post: Faz uma requisição GET à API do WordPress para obter o post.
    Verificação de Erro na Requisição: Verifica se a requisição foi bem-sucedida (status code 200).
    Extração e Tradução do Conteúdo: Extrai o título e o conteúdo do JSON da resposta e traduz usando googletrans.
    Publicação do Post Traduzido: Cria um novo post com o título e conteúdo traduzidos, e publica usando uma requisição POST à API do WordPress.
    Verificação de Erro na Publicação: Verifica se a publicação foi bem-sucedida (status code 201).

Certifique-se de substituir os valores no arquivo .env pelos seus valores reais de URL, credenciais, e configurações de idioma.




- Criada a v2

- Testando, erro:

ERRO

~~~~BASH

(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste# python3 script.py
Traceback (most recent call last):
  File "/teste/script.py", line 67, in <module>
    post_creator(source_url, base_url, source_language, target_language, "publish")
  File "/teste/script.py", line 33, in post_creator
    title_translation = translator.translate(get_article_title, src=sourceLang, dest=targetLang)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/teste/ambiente-virtual-novo/lib/python3.12/site-packages/googletrans/client.py", line 182, in translate
    data = self._translate(text, dest, src, kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/teste/ambiente-virtual-novo/lib/python3.12/site-packages/googletrans/client.py", line 78, in _translate
    token = self.token_acquirer.do(text)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/teste/ambiente-virtual-novo/lib/python3.12/site-packages/googletrans/gtoken.py", line 194, in do
    self._update()
  File "/teste/ambiente-virtual-novo/lib/python3.12/site-packages/googletrans/gtoken.py", line 62, in _update
    code = self.RE_TKK.search(r.text).group(1).replace('var ', '')
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'group'
(ambiente-virtual-novo) root@1c297bab36f0:/teste#

~~~~









O erro AttributeError: 'NoneType' object has no attribute 'group' geralmente ocorre quando a biblioteca googletrans não consegue obter o token de autenticação necessário para a tradução. Isso pode ser devido a mudanças na API do Google Translate, problemas temporários com o serviço ou a versão da biblioteca.

Para resolver isso, podemos tentar uma das seguintes abordagens:

    Atualizar a biblioteca googletrans: Verifique se está usando a versão mais recente da biblioteca googletrans.

    Usar uma biblioteca alternativa: Se a atualização não resolver o problema, considere usar uma biblioteca alternativa como deep-translator, que também oferece suporte para tradução com o Google Translate.

Aqui está um exemplo de como usar a biblioteca deep-translator:

Primeiro, instale a biblioteca:

sh

pip install deep-translator

Em seguida, atualize o script para usar deep-translator:

~~~~python

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
    get_article_title = data['title']['rendered']
    get_article_content = data['content']['rendered']

    translator = GoogleTranslator(source=sourceLang, target=targetLang)

    title_translation_text = translator.translate(get_article_title)
    content_translation_text = translator.translate(get_article_content)

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
~~~~

Explicação das Alterações:

    Substituição da Biblioteca: A biblioteca googletrans foi substituída pela deep-translator, que também fornece serviços de tradução utilizando o Google Translate.
    Uso de GoogleTranslator da deep-translator: A função GoogleTranslator é usada para traduzir o título e o conteúdo do post.

Essa abordagem deve contornar o problema com a biblioteca googletrans e permitir que você continue traduzindo e publicando posts no WordPress.





- Criando v3

~~~~python

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
    content_translation_text = translator.translate(get_article_content)

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
~~~~







- Teste

~~~~bash

(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste# python3 script.py
Conteúdo do post obtido:
{
    "id": 1,
    "date": "2024-05-11T12:14:35",
    "date_gmt": "2024-05-11T15:14:35",
    "guid": {
        "rendered": "https://palegreen-hornet-335449.hostingersite.com/?p=1"
    },
    "modified": "2024-05-11T12:14:35",
    "modified_gmt": "2024-05-11T15:14:35",
    "slug": "ola-mundo",
    "status": "publish",
    "type": "post",
    "link": "https://palegreen-hornet-335449.hostingersite.com/ola-mundo/",
    "title": {
        "rendered": "Olá, mundo!"
    },
    "content": {
        "rendered": "\n<p>Boas-vindas ao WordPress. Esse é o seu primeiro post. Edite-o ou exclua-o, e então comece a escrever!</p>\n",
        "protected": false
    },
    "excerpt": {
        "rendered": "<p>Boas-vindas ao WordPress. Esse é o seu primeiro post. Edite-o ou exclua-o, e então comece a escrever!</p>\n",
        "protected": false
    },
    "author": 1,
    "featured_media": 0,
    "comment_status": "open",
    "ping_status": "open",
    "sticky": false,
    "template": "",
    "format": "standard",
    "meta": {
        "site-sidebar-layout": "default",
        "site-content-layout": "",
        "ast-site-content-layout": "",
        "site-content-style": "default",
        "site-sidebar-style": "default",
        "ast-global-header-display": "",
        "ast-banner-title-visibility": "",
        "ast-main-header-display": "",
        "ast-hfb-above-header-display": "",
        "ast-hfb-below-header-display": "",
        "ast-hfb-mobile-header-display": "",
        "site-post-title": "",
        "ast-breadcrumbs-content": "",
        "ast-featured-img": "",
        "footer-sml-layout": "",
        "theme-transparent-header-meta": "",
        "adv-header-id-meta": "",
        "stick-header-meta": "",
        "header-above-stick-meta": "",
        "header-main-stick-meta": "",
        "header-below-stick-meta": "",
        "astra-migrate-meta-layouts": "default",
        "ast-page-background-enabled": "default",
        "ast-page-background-meta": {
            "desktop": {
                "background-color": "var(--ast-global-color-4)",
                "background-image": "",
                "background-repeat": "repeat",
                "background-position": "center center",
                "background-size": "auto",
                "background-attachment": "scroll",
                "background-type": "",
                "background-media": "",
                "overlay-type": "",
                "overlay-color": "",
                "overlay-gradient": ""
            },
            "tablet": {
                "background-color": "",
                "background-image": "",
                "background-repeat": "repeat",
                "background-position": "center center",
                "background-size": "auto",
                "background-attachment": "scroll",
                "background-type": "",
                "background-media": "",
                "overlay-type": "",
                "overlay-color": "",
                "overlay-gradient": ""
            },
            "mobile": {
                "background-color": "",
                "background-image": "",
                "background-repeat": "repeat",
                "background-position": "center center",
                "background-size": "auto",
                "background-attachment": "scroll",
                "background-type": "",
                "background-media": "",
                "overlay-type": "",
                "overlay-color": "",
                "overlay-gradient": ""
            }
        },
        "ast-content-background-meta": {
            "desktop": {
                "background-color": "var(--ast-global-color-5)",
                "background-image": "",
                "background-repeat": "repeat",
                "background-position": "center center",
                "background-size": "auto",
                "background-attachment": "scroll",
                "background-type": "",
                "background-media": "",
                "overlay-type": "",
                "overlay-color": "",
                "overlay-gradient": ""
            },
            "tablet": {
                "background-color": "var(--ast-global-color-5)",
                "background-image": "",
                "background-repeat": "repeat",
                "background-position": "center center",
                "background-size": "auto",
                "background-attachment": "scroll",
                "background-type": "",
                "background-media": "",
                "overlay-type": "",
                "overlay-color": "",
                "overlay-gradient": ""
            },
            "mobile": {
                "background-color": "var(--ast-global-color-5)",
                "background-image": "",
                "background-repeat": "repeat",
                "background-position": "center center",
                "background-size": "auto",
                "background-attachment": "scroll",
                "background-type": "",
                "background-media": "",
                "overlay-type": "",
                "overlay-color": "",
                "overlay-gradient": ""
            }
        },
        "footnotes": ""
    },
    "categories": [
        1
    ],
    "tags": [],
    "aioseo_notices": [],
    "_links": {
        "self": [
            {
                "href": "https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/posts/1"
            }
        ],
        "collection": [
            {
                "href": "https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/posts"
            }
        ],
        "about": [
            {
                "href": "https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/types/post"
            }
        ],
        "author": [
            {
                "embeddable": true,
                "href": "https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/users/1"
            }
        ],
        "replies": [
            {
                "embeddable": true,
                "href": "https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/comments?post=1"
            }
        ],
        "version-history": [
            {
                "count": 0,
                "href": "https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/posts/1/revisions"
            }
        ],
        "wp:attachment": [
            {
                "href": "https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/media?parent=1"
            }
        ],
        "wp:term": [
            {
                "taxonomy": "category",
                "embeddable": true,
                "href": "https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/categories?post=1"
            },
            {
                "taxonomy": "post_tag",
                "embeddable": true,
                "href": "https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/tags?post=1"
            }
        ],
        "curies": [
            {
                "name": "wp",
                "href": "https://api.w.org/{rel}",
                "templated": true
            }
        ]
    }
}
Post publicado com sucesso!
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste# date
Sat May 25 22:23:36 -03 2024
(ambiente-virtual-novo) root@1c297bab36f0:/teste#

~~~~





- OK
v3 funcionando!


- OK
v3 funcionando!
- OK
v3 funcionando!
- OK
v3 funcionando!










## Dia 26/05/2024



# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## PENDENTE

- Testar com o Blog devopsmind.
- Fixar versões contidas no "requirements.txt", definir versões exatas.
- Criar Dockerfile e docker-compose, posteriormente.
- Ver forma de acionar fácil o script para um blog e post especifico. Usar Makefile +CLI??? Variar ambiente virtual??? Avaliar as opções.
- Adicionar try, exception, logs de erros.
- Testar combo "Fedora 40 + PyTorch" , <https://www.tudocelular.com/tech/noticias/n219464/fedora-linux-40-beta-lancado-gnome-46-ia.html>









- Testar com o Blog devopsmind.

- ERRO

~~~~BASH

}
Traceback (most recent call last):
  File "/devopsmind/script.py", line 68, in <module>
    post_creator(source_url, base_url, source_language, target_language, "publish")
  File "/devopsmind/script.py", line 38, in post_creator
    content_translation_text = translator.translate(get_article_content)
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/teste/ambiente-virtual-novo/lib/python3.12/site-packages/deep_translator/google.py", line 57, in translate
    if is_input_valid(text, max_chars=5000):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/teste/ambiente-virtual-novo/lib/python3.12/site-packages/deep_translator/validate.py", line 41, in is_input_valid
    raise NotValidLength(text, min_chars, max_chars)
deep_translator.exceptions.NotValidLength:
<nav class="wp-block-stackable-table-of-contents stk-block-table-of-contents stk-block stk-957d752" data-block-id="957d752"><p class="stk-table-of-contents__title">Tópicos</p><ul class="stk-table-of-contents__table"><li><a href="#introducao">Introdução</a><ul><li><a href="#ideia">Ideia</a></li></ul></li><li><a href="#script-para-limpeza-de-branches">Script para limpeza de branches</a><ul><li><a href="#explicacao-detalhada">Explicação detalhada</a></li></ul></li><li><a href="#importante">Importante</a></li><li><a href="#material-de-apoio">Material de apoio</a></li><li><a href="#conclusao">Conclusão</a></li></ul></nav>


 --> Text length need to be between 0 and 5000 characters
~~~~



ERRO PARECE SER DE MAXIMO DE CARACTERES DO DEEP





I'd be glad to help you resolve the Text length need to be between 0 and 5000 characters error in your deep_translator script.

Error Explanation:

This error occurs because the deep_translator library has a built-in limitation where the text you want to translate cannot exceed 5,000 characters. The library raises a NotValidLength exception when you attempt to translate a text longer than this limit.

Solutions:

    Split the Text into Chunks:

    The most straightforward approach is to divide your large text into smaller chunks, each under 5,000 characters. Then, translate each chunk individually and combine the translated parts back into the complete text.

    Here's an example using Python:

~~~~Python
    import deep_translator

    def translate_large_text(text, source_language, target_language):
        chunk_size = 4500  # Adjust chunk size as needed
        translated_chunks = []
        for i in range(0, len(text), chunk_size):
            chunk = text[i:i+chunk_size]
            translated_chunks.append(deep_translator.translate(chunk, source_language, target_language))
        return ''.join(translated_chunks)

    source_url = "..."  # Your source URL
    base_url = "..."   # Your base URL (if applicable)
    source_language = "..."  # Source language code
    target_language = "..."  # Target language code

    get_article_content = # Your function to get the article content

    translated_content = translate_large_text(get_article_content(), source_language, target_language)

    # ... (Use the translated_content)
~~~~

    Use o código com cuidado.

    Consider Alternative Translation Libraries:

    If you frequently deal with large texts, you might explore translation libraries that offer higher character limits or support chunking internally. Some options include:
        Google Translate API: You can use the Google Translate API directly (requires an API key), which allows for larger character limits depending on your pricing tier.
        Azure Cognitive Services Translator: This service offers similar functionality to Google Translate and potentially higher character limits depending on your plan.

Choosing the Right Solution:

    For occasional use: If you only need to translate large texts occasionally, splitting them into chunks is a practical approach.
    For frequent use: If you regularly work with large texts, a different translation library or the Google Translate/Azure Translator API might be more efficient.

Additional Tips:

    Adjust the chunk_size in the first solution based on your needs and the library's limitations.
    If you encounter errors specific to the Google Translate API or Azure Translator, refer to their respective documentation for troubleshooting.

By implementing one of these solutions, you should be able to handle larger texts in your deep_translator script and avoid the character limit error.





O erro que você está enfrentando é causado pelo fato de que o texto que está sendo passado para a função de tradução excede o limite de caracteres permitido pela biblioteca deep_translator. O limite máximo é de 5000 caracteres.

Para resolver esse problema, você pode dividir o texto em partes menores, cada uma com no máximo 5000 caracteres, antes de passá-las para a função de tradução. Aqui está um exemplo de como você pode fazer isso:
Passos

    Divida o texto em partes menores:
        Crie uma função para dividir o texto em partes menores com no máximo 5000 caracteres.

    Traduza cada parte separadamente:
        Traduza cada parte separadamente e depois combine os resultados.

Exemplo de Implementação

Aqui está um exemplo de como você pode implementar isso no seu código:

~~~~python

def dividir_texto(texto, tamanho_max):
    """Divide o texto em partes menores de acordo com o tamanho máximo especificado."""
    return [texto[i:i + tamanho_max] for i in range(0, len(texto), tamanho_max)]

def traduzir_texto(texto, translator):
    """Traduz o texto dividindo-o em partes menores se necessário."""
    partes = dividir_texto(texto, 5000)
    partes_traduzidas = [translator.translate(parte) for parte in partes]
    return ' '.join(partes_traduzidas)

def post_creator(source_url, base_url, source_language, target_language, action):
    # ... (outros códigos do seu script)
    content_translation_text = traduzir_texto(get_article_content, translator)
    # ... (continuação do seu script)

# Exemplo de uso:
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='auto', target='en')

source_url = "http://example.com/source"
base_url = "http://example.com"
source_language = "pt"
target_language = "en"

post_creator(source_url, base_url, source_language, target_language, "publish")
~~~~

Explicação

    Função dividir_texto:
        Esta função divide o texto em partes menores com no máximo 5000 caracteres.

    Função traduzir_texto:
        Esta função usa a função dividir_texto para dividir o texto original e, em seguida, traduz cada parte separadamente. Finalmente, combina as partes traduzidas em um único texto.

    Modificação na post_creator:
        Substituímos a chamada direta para translator.translate pela função traduzir_texto para garantir que o texto seja dividido e traduzido corretamente.

Considerações

    Limite de Caracteres:
        Certifique-se de que o limite de 5000 caracteres é apropriado para a função de tradução que você está usando. Se a biblioteca deep_translator tiver um limite diferente, ajuste o código conforme necessário.

    Concatenar Partes Traduzidas:
        O exemplo acima combina as partes traduzidas com um espaço (' '.join(partes_traduzidas)). Dependendo do seu caso de uso, você pode precisar de um delimitador diferente ou de algum tratamento adicional para garantir que a tradução final esteja correta.

Dessa forma, você conseguirá traduzir textos longos sem ultrapassar o limite de caracteres permitido pela biblioteca de tradução.





- ERRO

~~~~BASH

}
Traceback (most recent call last):
  File "/devopsmind/script.py", line 68, in <module>
    post_creator(source_url, base_url, source_language, target_language, "publish")
  File "/devopsmind/script.py", line 38, in post_creator
    content_translation_text = translator.translate(get_article_content)
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/teste/ambiente-virtual-novo/lib/python3.12/site-packages/deep_translator/google.py", line 57, in translate
    if is_input_valid(text, max_chars=5000):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/teste/ambiente-virtual-novo/lib/python3.12/site-packages/deep_translator/validate.py", line 41, in is_input_valid
    raise NotValidLength(text, min_chars, max_chars)
deep_translator.exceptions.NotValidLength:
<nav class="wp-block-stackable-table-of-contents stk-block-table-of-contents stk-block stk-957d752" data-block-id="957d752"><p class="stk-table-of-contents__title">Tópicos</p><ul class="stk-table-of-contents__table"><li><a href="#introducao">Introdução</a><ul><li><a href="#ideia">Ideia</a></li></ul></li><li><a href="#script-para-limpeza-de-branches">Script para limpeza de branches</a><ul><li><a href="#explicacao-detalhada">Explicação detalhada</a></li></ul></li><li><a href="#importante">Importante</a></li><li><a href="#material-de-apoio">Material de apoio</a></li><li><a href="#conclusao">Conclusão</a></li></ul></nav>


 --> Text length need to be between 0 and 5000 characters
~~~~





# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## PENDENTE

- Tratar erro  "--> Text length need to be between 0 and 5000 characters" do deep_translator. Avaliar opções, como criar função para dividir o texto em chunks menores, etc.
- Testar com o Blog devopsmind.
- Fixar versões contidas no "requirements.txt", definir versões exatas.
- Criar Dockerfile e docker-compose, posteriormente.
- Ver forma de acionar fácil o script para um blog e post especifico. Usar Makefile +CLI??? Variar ambiente virtual??? Avaliar as opções.
- Adicionar try, exception, logs de erros.
- Testar combo "Fedora 40 + PyTorch" , <https://www.tudocelular.com/tech/noticias/n219464/fedora-linux-40-beta-lancado-gnome-46-ia.html>









- Tratar erro  "--> Text length need to be between 0 and 5000 characters" do deep_translator. Avaliar opções, como criar função para dividir o texto em chunks menores, etc.




Para adaptar o código para que o conteúdo do post seja quebrado em partes menores do que 4500 caracteres, você pode dividir o texto em pedaços antes de fazer a tradução e postagem. Aqui está uma versão adaptada do seu código que faz isso:

python

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

Neste código, a função split_text divide o texto do conteúdo em partes menores que 4500 caracteres. Em seguida, essas partes são traduzidas individualmente e concatenadas de volta em um único texto traduzido. Isso garante que o conteúdo não ultrapasse o limite de caracteres durante a tradução.



- Criando a v4 para teste
/home/fernando/cursos/python/wordpress-blog-post-with-python/testes/script-v4.py

~~~~bash
Post publicado com sucesso!
(ambiente-virtual-novo) root@1c297bab36f0:/devopsmind# date
Sun May 26 22:55:47 -03 2024
(ambiente-virtual-novo) root@1c297bab36f0:/devopsmind#
~~~~


- OK

CRIOU O POST
<https://devopsmind.com.br/en/git-en/automating-branch-cleanup-in-git/>


- OK

CRIOU O POST
<https://devopsmind.com.br/en/git-en/automating-branch-cleanup-in-git/>


- OK

CRIOU O POST
<https://devopsmind.com.br/en/git-en/automating-branch-cleanup-in-git/>


~~~~bash

fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ git add .
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ git commit -m "OK, adicionando ajuste que quebra os chunks em até 4500 caracteres, para atender a limitação da biblioteca do Deep."
[main c9b0150] OK, adicionando ajuste que quebra os chunks em até 4500 caracteres, para atender a limitação da biblioteca do Deep.
 4 files changed, 331 insertions(+), 5 deletions(-)
 create mode 100644 testes/script-v3-b.py
 create mode 100644 testes/script-v4.py
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$ git push
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 8 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 1.98 KiB | 1.98 MiB/s, done.
Total 5 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To github.com:fernandomullerjr/wordpress-blog-post-with-python.git
   4da40fd..c9b0150  main -> main
fernando@debian10x64:~/cursos/python/wordpress-blog-post-with-python$


~~~~





# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## PENDENTE

**MELHORIAS, V2** - Fazer que o post traduzido seja criado com Editor Wordpress avançado, ao invés do editor clássico. Que algumas formatações não se percam.
**MELHORIAS, v3**, Ver como pegar no JSON a capa do Post, imagem destaque, definir categoria, linguagem,  etc. Verificar demais melhoriais que é possível realizar.
- MELHORIAS, Ver como pegar no JSON a capa do Post, imagem destaque, definir categoria, linguagem,  etc. Verificar demais melhoriais que é possível realizar.
- Testar com o Blog devopsmind.
- Fixar versões contidas no "requirements.txt", definir versões exatas.
- Criar Dockerfile e docker-compose, posteriormente. Avaliar melhores práticas.
- Ver forma de acionar fácil o script para um blog e post especifico, chamar uma CLI que vai perguntando os dados desejados. Usar Makefile +CLI??? Variar ambiente virtual??? Avaliar as opções.
- Ver como obter os JSON de blogs do exterior e automatizar o processo de criar um post, com base na página do exterior, adicionar menções ao DevOps Mind no cabeçalho.
- Adicionar try, exception, logs de erros.
- Testar combo "Fedora 40 + PyTorch" , <https://www.tudocelular.com/tech/noticias/n219464/fedora-linux-40-beta-lancado-gnome-46-ia.html>











# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## Dia 11/07/2024

Testes para v2

**MELHORIAS, V2** - Fazer que o post traduzido seja criado com Editor Wordpress avançado, ao invés do editor clássico. Que algumas formatações não se percam.


1. Iniciar o container Docker.
2. Conectar no container.
3. Carregar o ambiente virtual do Python.
4. Executar o script em Python.

Seguem os comandos utilizados:

```bash
docker start ubuntu
docker container exec -ti ubuntu bash
source /teste/ambiente-virtual-novo/bin/activate
# Editar o .env com o id do Post desejado
python3 script.py
```



criando post
"Docker, SRE e DevOps: Uma Abordagem Integrada para Confiabilidade e Eficiência"
https://palegreen-hornet-335449.hostingersite.com/wp-admin/post.php?post=3282&action=edit

<https://palegreen-hornet-335449.hostingersite.com/docker-sre-e-devops-uma-abordagem-integrada-para-confiabilidade-e-eficiencia/>


- Executando
python3 script.py

~~~~bash
<p>Espero que este post seja útil para os leitores! <a href="https://roadmap.sh/devops/devops-vs-sre" target="_blank" rel="noopener">Se tiver alguma pergunta adicional, estou à disposição. 😊🚀</a><a href="https://roadmap.sh/devops/devops-vs-sre" target="_blank" rel="noreferrer noopener"><sup>1</sup></a><a href="https://srestuff.com.br/" target="_blank" rel="noreferrer noopener"><sup>2</sup></a><a href="https://stackoverflow.com/questions/63043718/who-should-write-the-dockerfile-sre-or-developer" target="_blank" rel="noreferrer noopener"><sup>3</sup></a><a href="https://roadmap.sh/devops" target="_blank" rel="noreferrer noopener"><sup>4</sup></a></p>
<p><a href="https://roadmap.sh/devops/devops-vs-sre" target="_blank" rel="noopener"></a><a href="https://roadmap.sh/devops/devops-vs-sre" target="_blank" rel="noreferrer noopener"><sup>1</sup></a>: <a is="cib-link" href="https://roadmap.sh/devops/devops-vs-sre" target="_blank" rel="noreferrer noopener">DevOps vs SRE: Key Differences Explained</a><a href="https://roadmap.sh/devops/devops-vs-sre" target="_blank" rel="noopener"> </a><a href="https://srestuff.com.br/" target="_blank" rel="noreferrer noopener"><sup>2</sup></a>: <a is="cib-link" href="https://srestuff.com.br/" target="_blank" rel="noreferrer noopener">SRE Stuff &#8211; Empowering DevOps and Cloud Technologies</a><a href="https://roadmap.sh/devops/devops-vs-sre" target="_blank" rel="noopener"> </a><a href="https://stackoverflow.com/questions/63043718/who-should-write-the-dockerfile-sre-or-developer" target="_blank" rel="noreferrer noopener"><sup>3</sup></a>: <a is="cib-link" href="https://stackoverflow.com/questions/63043718/who-should-write-the-dockerfile-sre-or-developer" target="_blank" rel="noreferrer noopener">Who should write the dockerfile, SRE or developer?</a><a href="https://roadmap.sh/devops/devops-vs-sre" target="_blank" rel="noopener"> </a><a href="https://roadmap.sh/devops" target="_blank" rel="noreferrer noopener"><sup>4</sup></a>: <a is="cib-link" href="https://roadmap.sh/devops" target="_blank" rel="noreferrer noopener">DevOps Roadmap: Learn to become a DevOps Engineer or SRE</a></p>
 --> Text length need to be between 0 and 5000 characters
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste# date
Thu Jul 11 23:46:58 -03 2024
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
~~~~


git add .
git commit -m "TESTES da V2 - Wordpress with Python."
git push



- ERRO
verificando a saída do script
tem erro devido input

~~~~bash
  ]
    }
}
Traceback (most recent call last):
  File "/teste/script.py", line 68, in <module>
    post_creator(source_url, base_url, source_language, target_language, "publish")
  File "/teste/script.py", line 38, in post_creator
    content_translation_text = translator.translate(get_article_content)
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/teste/ambiente-virtual-novo/lib/python3.12/site-packages/deep_translator/google.py", line 57, in translate
    if is_input_valid(text, max_chars=5000):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/teste/ambiente-virtual-novo/lib/python3.12/site-packages/deep_translator/validate.py", line 41, in is_input_valid
    raise NotValidLength(text, min_chars, max_chars)
deep_translator.exceptions.NotValidLength:
<hr class="wp-block-separator has-alpha-channel-opacity"/>
~~~~



- Pasta "teste" está com o script obsoleto, que não faz split em partes menores do JSON.
copiando o script novo pra pasta
cp /devopsmind/script.py .

- Pasta "teste" está com o script obsoleto, que não faz split em partes menores do JSON.
copiando o script novo pra pasta
cp /devopsmind/script.py .
- Pasta "teste" está com o script obsoleto, que não faz split em partes menores do JSON.
copiando o script novo pra pasta
cp /devopsmind/script.py .
- Pasta "teste" está com o script obsoleto, que não faz split em partes menores do JSON.
copiando o script novo pra pasta
cp /devopsmind/script.py .

- Novo teste OK:

~~~~bash
     }
        ],
        "wp:term": [
            {
                "taxonomy": "category",
                "embeddable": true,
                "href": "https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/categories?post=3282"
            },
            {
                "taxonomy": "post_tag",
                "embeddable": true,
                "href": "https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/tags?post=3282"
            }
        ],
        "curies": [
            {
                "name": "wp",
                "href": "https://api.w.org/{rel}",
                "templated": true
            }
        ]
    }
}
Post publicado com sucesso!
(ambiente-virtual-novo) root@1c297bab36f0:/teste#


(ambiente-virtual-novo) root@1c297bab36f0:/teste# date
Thu Jul 11 23:52:28 -03 2024
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
 29  cp /devopsmind/script.py .
   30  ls -lhasp
   31  python3 script.py
   32  date
   33  history | tail
(ambiente-virtual-novo) root@1c297bab36f0:/teste# ls -lhasp
total 20K
4.0K drwxr-xr-x 3 root root 4.0K Jul 11 23:46 ./
4.0K drwxr-xr-x 1 root root 4.0K May 26 13:12 ../
4.0K -rw-r--r-- 1 root root  301 Jul 11 23:46 .env
4.0K drwxr-xr-x 5 root root 4.0K May 12 11:36 ambiente-virtual-novo/
4.0K -rw-r--r-- 1 root root 2.7K Jul 11 23:51 script.py
(ambiente-virtual-novo) root@1c297bab36f0:/teste#

~~~~

- Gerou o post traduzido:
<https://palegreen-hornet-335449.hostingersite.com/docker-sre-and-devops-an-integrated-approach-for-reliability-and-efficiency/>
TOC veio em editor clássico.

- Versão atual que foi utilizada:
/home/fernando/cursos/python/wordpress-blog-post-with-python/testes/script-v4.py








## GPT

Para garantir que o seu script Python crie um novo post no WordPress com o editor de blocos (Gutenberg), você precisa ajustar o formato do conteúdo enviado para o endpoint da API REST do WordPress. O Gutenberg utiliza um formato específico para os blocos de conteúdo, que inclui tanto o HTML renderizado quanto metadados adicionais para cada bloco.

Aqui estão as modificações necessárias no seu script para que o conteúdo seja formatado corretamente para o editor de blocos do WordPress:

    Formatando o Conteúdo para Gutenberg:
        Cada bloco de conteúdo no Gutenberg é representado por um objeto JSON dentro de um array chamado blocks.
        Cada objeto de bloco tem um tipo (por exemplo, paragraph, heading, list, etc.) e um conjunto de atributos específicos para aquele tipo de bloco.

    Atualizando o Payload JSON:
        O payload JSON que você envia para criar o post no WordPress deve incluir uma chave blocks com uma lista de objetos de bloco formatados corretamente.

    Exemplo de Conversão do Conteúdo:
        Vamos assumir que o conteúdo traduzido já está no formato de texto simples. Você precisará converter isso em um formato adequado para o Gutenberg.

Aqui está um exemplo de como você pode ajustar o seu script para formatar o conteúdo para o editor de blocos do WordPress:

~~~~python

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

    # Converte o conteúdo traduzido para o formato de blocos do Gutenberg
    blocks = []
    for paragraph in content_translation_text.split('\n'):
        blocks.append({
            "type": "paragraph",
            "data": {
                "text": paragraph.strip()
            }
        })

    WP_url = wpBaseURL + "/wp-json/wp/v2/posts"

    auth = HTTPBasicAuth(wp_app_username, wp_app_password)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "status": postStatus,
        "title": title_translation_text,
        "content": {
            "blocks": blocks
        }
    }

    response = requests.post(
        WP_url,
        json=payload,
        headers=headers,
        auth=auth
    )

    if response.status_code == 201:
        print("Post publicado com sucesso!")
    else:
        print(f"Erro ao publicar o post: {response.status_code}")
        print(response.json())

post_creator(source_url, base_url, source_language, target_language, "publish")
~~~~

Neste exemplo ajustado:

    content_parts é dividido em parágrafos individuais.
    Cada parágrafo traduzido é formatado como um bloco de tipo paragraph.
    O payload agora inclui content com a chave blocks contendo a lista de blocos formatados corretamente.

Com essas alterações, seu script Python deve criar corretamente um novo post no WordPress com o editor de blocos (Gutenberg), refletindo o conteúdo traduzido de forma adequada e estruturada. Certifique-se de testar o script em um ambiente de desenvolvimento antes de aplicá-lo em produção.






## COPILOT

Para criar um post no WordPress com o conteúdo em blocos, você precisa formatar o conteúdo do post em um formato específico que o WordPress reconheça como blocos. O WordPress usa uma estrutura chamada "Gutenberg blocks" para o editor de blocos. Para enviar conteúdo nesse formato, você precisa estruturar o conteúdo do post como uma série de blocos em JSON.

Aqui está um exemplo de como você pode modificar o seu script para criar um post com conteúdo em blocos:

Converter o Conteúdo Traduzido em Blocos: Antes de enviar o conteúdo para o WordPress, converta o texto traduzido em uma estrutura de blocos. Cada parágrafo pode ser um bloco separado, por exemplo.

Modificar o Payload: Use a estrutura de blocos no payload da requisição POST para criar o post.

Segue um exemplo de como fazer isso:

~~~~PYTHON
# Função para converter o conteúdo traduzido em blocos Gutenberg
def convert_to_blocks(content):
    paragraphs = content.split('\n')  # Supondo que cada parágrafo é separado por uma nova linha
    blocks = []
    for paragraph in paragraphs:
        if paragraph:  # Ignora linhas vazias
            block = {
                "blockName": "core/paragraph",
                "attrs": {},
                "innerBlocks": [],
                "innerHTML": paragraph,
                "innerContent": [paragraph],
            }
            blocks.append(block)
    return blocks

# Modifique a parte do script onde o payload é criado
content_blocks = convert_to_blocks(content_translation_text)
payload = json.dumps({
    "status": postStatus,
    "title": title_translation_text,
    "content": "",  # O conteúdo agora vai nos blocos
    "blocks": content_blocks  # Adiciona os blocos aqui
})

~~~~


Nota Importante: Este exemplo assume que você está trabalhando com um WordPress que suporta a criação de posts com conteúdo em blocos via API REST. Certifique-se de que sua versão do WordPress e sua configuração permitem isso. Além disso, a estrutura de blocos pode precisar de ajustes dependendo de como você deseja que o conteúdo apareça e quais tipos de blocos você está usando.



- Criando v5 para testes, baseada no GPT:
/home/fernando/cursos/python/wordpress-blog-post-with-python/testes/script-v5.py


- Testando

~~~~bash
Post publicado com sucesso!
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste# date
Fri Jul 12 00:19:28 -03 2024
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
~~~~

não ok

- Criou um post apenas com titulo, sem conteudo, conteudo vazio:
https://palegreen-hornet-335449.hostingersite.com/wp-admin/post.php?post=3290&action=edit



- Criando a v6 baseada no Copilot
/home/fernando/cursos/python/wordpress-blog-post-with-python/testes/script-v6.py

- Testando

~~~~bash
Post publicado com sucesso!
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
(ambiente-virtual-novo) root@1c297bab36f0:/teste# date
Fri Jul 12 00:26:13 -03 2024
(ambiente-virtual-novo) root@1c297bab36f0:/teste#
~~~~


não ok

- Criou um post apenas com titulo, sem conteudo, conteudo vazio:
https://palegreen-hornet-335449.hostingersite.com/wp-admin/post.php?post=3292&action=edit




<https://community.zapier.com/how-do-i-3/how-to-create-wordpress-post-using-block-editor-instead-of-classic-editor-in-zapier-28770>
Hi @Kriswuhk, welcome to the Community! 👋

I’ve been looking into this and it seems that the WordPress API doesn’t actually have the ability to select the block editor when creating a post. The options currently available for their “Create a Post” endpoint can be viewed here: https://developer.wordpress.org/rest-api/reference/posts/#create-a-post




# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## PENDENTE

- V2 com GPT e/ou Copilot
ver como fazer:
    Converter post para Editor em Blocos ao invés do Editor Clássico.
    Ajustar HREFLANG do Post.
    Tratar para que o TOC(Table of Contents) venha corretamente.
Ver idéia: <https://automatevalue.com/blog/wordpress-blocks-post-using-the-rest-api/>
<https://jeremyrichardson.dev/blog/parsing-a-raw-wordpress-post-with-blocks>
<https://community.zapier.com/how-do-i-3/how-to-create-wordpress-post-using-block-editor-instead-of-classic-editor-in-zapier-28770>
<https://developer.wordpress.org/rest-api/reference/posts/#create-a-post>
possível solução:
<https://myshittycode.com/2023/01/03/wordpress-creating-gutenberg-block-compatible-posts-using-rest-api/>

**MELHORIAS, V2** - Fazer que o post traduzido seja criado com Editor Wordpress avançado, ao invés do editor clássico. Que algumas formatações não se percam.
**MELHORIAS, v3**, Ver como pegar no JSON a capa do Post, imagem destaque, definir categoria, linguagem,  etc. Verificar demais melhoriais que é possível realizar.
- MELHORIAS, Ver como pegar no JSON a capa do Post, imagem destaque, definir categoria, linguagem,  etc. Verificar demais melhoriais que é possível realizar.
- Testar com o Blog devopsmind.
- Fixar versões contidas no "requirements.txt", definir versões exatas.
- Criar Dockerfile e docker-compose, posteriormente. Avaliar melhores práticas.
- Ver forma de acionar fácil o script para um blog e post especifico, chamar uma CLI que vai perguntando os dados desejados. Usar Makefile +CLI??? Variar ambiente virtual??? Avaliar as opções.
- Ver como obter os JSON de blogs do exterior e automatizar o processo de criar um post, com base na página do exterior, adicionar menções ao DevOps Mind no cabeçalho.
- Adicionar try, exception, logs de erros.
- Testar combo "Fedora 40 + PyTorch" , <https://www.tudocelular.com/tech/noticias/n219464/fedora-linux-40-beta-lancado-gnome-46-ia.html>








1. Iniciar o container Docker.
2. Conectar no container.
3. Carregar o ambiente virtual do Python.
4. Executar o script em Python.

Seguem os comandos utilizados:

```bash
docker start ubuntu
docker container exec -ti ubuntu bash
source /teste/ambiente-virtual-novo/bin/activate
# Acessar o diretório contendo o devido script e .env
cd /devopsmind
# ou /teste, para uso no Blog adicional
cd /teste
# Editar o .env com o id do Post desejado, editando a variável SOURCE_URL, ao final o número é obtido na página "Posts", passando o mouse por cima de um post e vendo seu id
python3 script.py
```



Para ajustar o código para lidar com diferentes tipos de blocos, como parágrafos, imagens, títulos (h1, h2, etc.), e table of contents no WordPress, você precisará analisar o conteúdo HTML original e converter cada elemento HTML relevante em seu respectivo bloco Gutenberg. Aqui está um plano de como você pode fazer isso:

Analisar o HTML: Use uma biblioteca de parsing de HTML como BeautifulSoup para analisar o conteúdo HTML obtido do post original.

Identificar Elementos: Identifique os diferentes elementos HTML (como <p>, <img>, <h1>, <h2>, etc.) e converta cada um deles em seu respectivo bloco Gutenberg.

Criar Blocos Gutenberg: Para cada tipo de elemento, crie um dicionário Python que represente o bloco Gutenberg correspondente.

Montar os Blocos: Combine todos os blocos criados em uma lista que representará o conteúdo completo do post em formato de blocos.

Segue um exemplo de como você pode começar a implementar essas etapas:

~~~~python
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

def html_to_blocks(html_content, sourceLang, targetLang):
    soup = BeautifulSoup(html_content, 'html.parser')
    blocks = []
    translator = GoogleTranslator(source=sourceLang, target=targetLang)

    for element in soup.children:
        if element.name == 'p':
            translated_text = translator.translate(element.text)
            blocks.append({
                "blockName": "core/paragraph",
                "attrs": {},
                "innerBlocks": [],
                "innerHTML": translated_text,
                "innerContent": [translated_text],
            })
        elif element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            translated_text = translator.translate(element.text)
            blocks.append({
                "blockName": f"core/heading",
                "attrs": {"level": int(element.name[1])},
                "innerBlocks": [],
                "innerHTML": translated_text,
                "innerContent": [translated_text],
            })
        elif element.name == 'img':
            # Supondo que a imagem não precisa ser traduzida, mas você pode adicionar lógica aqui se necessário
            blocks.append({
                "blockName": "core/image",
                "attrs": {
                    "url": element['src'],
                    "alt": element.get('alt', '')
                },
                "innerBlocks": [],
                "innerHTML": '',
                "innerContent": [],
            })
        # Adicione mais condições conforme necessário para outros tipos de blocos

    return blocks

# Use a função html_to_blocks no lugar onde você cria os blocos Gutenberg
content_blocks = html_to_blocks(get_article_content, source_language, target_language)
~~~~

Nota: Este exemplo usa BeautifulSoup para analisar o HTML e identificar diferentes tipos de elementos. Para cada tipo de elemento, ele cria um bloco Gutenberg correspondente. Você precisará instalar a biblioteca BeautifulSoup (beautifulsoup4) e talvez atualizar a biblioteca deep_translator para a versão mais recente, se ainda não o fez.

Este é um ponto de partida. Dependendo da complexidade do HTML do seu conteúdo e dos tipos específicos de blocos que você deseja suportar, você pode precisar expandir e ajustar a lógica de conversão.

- Validando que o bs4 está instalado:

~~~~bash
(ambiente-virtual-novo) root@1c297bab36f0:/teste# pip3 list
Package            Version
------------------ --------
beautifulsoup4     4.12.3
certifi            2024.2.2
chardet            3.0.4
charset-normalizer 3.3.2
deep-translator    1.11.4
googletrans        3.0.0
h11                0.9.0
h2                 3.2.0
hpack              3.0.0
hstspreload        2024.5.1
httpcore           0.9.1
httpx              0.13.3
hyperframe         5.2.0
idna               2.10
pip                24.0
python-dotenv      1.0.1
requests           2.31.0
rfc3986            1.5.0
sniffio            1.3.1
soupsieve          2.5
urllib3            2.2.1
(ambiente-virtual-novo) root@1c297bab36f0:/teste#

~~~~


- Criando a v7
/home/fernando/cursos/python/wordpress-blog-post-with-python/testes/script-v7.py


git status
git add .
git commit -m "Testando laço para criar blocos Gutemberg."
git push
git status


- Testando
não funcionou

- Trouxe um post com o código abaixo, não é bem o eu queria ;s

[{“blockName”: “core/heading”, “attrs”: {“level”: 1}, “innerBlocks”: [], “innerHTML”: “Introduction”, “innerContent”: [“Introduction”]}, {“blockName”: “core/paragraph”, “attrs”: {}, “innerBlocks”: [], “innerHTML”: “The world of technology is constantly evolving, and managing complex systems requires innovative approaches. In this context, two methodologies stand out: DevOps and Site Reliability Engineering (SRE). Both aim to improve software delivery and operational efficiency. And Docker, a container virtualization tool, plays a fundamental role in this scenario.”, “innerContent”: [“The world of technology is constantly evolving, and managing complex systems requires innovative approaches. In this context, two methodologies stand out: DevOps and Site Reliability Engineering (SRE). Both aim to improve software delivery and operational efficiency. And Docker, a container virtualization tool, plays a fundamental role in this scenario.”]}, {“blockName”: “core/heading”, “attrs”: {“level”: 3}, “innerBlocks”: [], “innerHTML”: “DevOps and SRE: What Are They?”, “innerContent”: [“DevOps and SRE: What Are They?”]}, {“blockName”: “core/heading”, “attrs”: {“level”: 2}, “innerBlocks”: [], “innerHTML”: “Main Content”, “innerContent”: [“Main Content”]}, {“blockName”: “core/heading”, “attrs”: {“level”: 3}, “innerBlocks”: [], “innerHTML”: “Essential Practices with Docker”, “innerContent”: [“Essential Practices with Docker”]}, {“blockName”: “core/heading”, “attrs”: {“level”: 3}, “innerBlocks”: [], “innerHTML”: “Tools and Technologies”, “innerContent”: [“Tools and Technologies”]}, {“blockName”: “core/heading”, “attrs”: {“level”: 3}, “innerBlocks”: [], “innerHTML”: “Benefits and Challenges”, “innerContent”: [“Benefits and Challenges”]}, {“blockName”: “core/heading”, “attrs”: {“level”: 2}, “innerBlocks”: [], “innerHTML”: “Examples of Success Stories”, “innerContent”: [“Examples of Success Stories”]}, {“blockName”: “core/heading”, “attrs”: {“level”: 2}, “innerBlocks”: [], “innerHTML”: “Conclusion”, “innerContent”: [“Conclusion”]}, {“blockName”: “core/paragraph”, “attrs”: {}, “innerBlocks”: [], “innerHTML”: “Docker is a key piece of the DevOps and SRE puzzle. By adopting this technology, companies can improve the reliability, efficiency and scalability of their systems. Want to know more? Visit the DevOps Mind blog for exclusive insights and ongoing updates.”, “innerContent”: [“Docker is a key piece of the DevOps and SRE puzzle. By adopting this technology, companies can improve the reliability, efficiency and scalability of their systems. Want to know more? Visit the DevOps Mind blog for exclusive insights and ongoing updates.”]}, {“blockName”: “core/paragraph”, “attrs”: {}, “innerBlocks”: [], “innerHTML”: “I hope this post is useful for readers! If you have any additional questions, I am at your disposal. \ud83d\ude0a\ud83d\ude801234”, “innerContent”: [“I hope this post is useful for readers! If you have any additional questions, I am at your disposal. \ud83d\ude0a\ud83d\ude801234”]}, {“blockName”: “core/paragraph”, “attrs”: {}, “innerBlocks”: [], “innerHTML”: “1: DevOps vs SRE: Key Differences Explained 2: SRE Stuff \u2013 Empowering DevOps and Cloud Technologies 3: Who should write the dockerfile, SRE or developer? 4: DevOps Roadmap: Learn to become a DevOps Engineer or SRE”, “innerContent”: [“1: DevOps vs SRE: Key Differences Explained 2: SRE Stuff \u2013 Empowering DevOps and Cloud Technologies 3: Who should write the dockerfile, SRE or developer? 4: DevOps Roadmap: Learn to become a DevOps Engineer or SRE”]}]








- Idéia nova
<https://myshittycode.com/2023/01/03/wordpress-creating-gutenberg-block-compatible-posts-using-rest-api/>




seguindo esta idéia:
https://myshittycode.com/2023/01/03/wordpress-creating-gutenberg-block-compatible-posts-using-rest-api/

como eu faria algo equivalente usando python?

Ótima sugestão! Vamos adaptar o código com base no exemplo fornecido no link. Aqui está uma versão em Python que cria posts no WordPress usando o editor de blocos do Gutenberg:

~~~~python

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

    # Cria os blocos de conteúdo do Gutenberg
    content_blocks = [
        create_gutenberg_block("core/paragraph", {}, [], content_translation_text)
    ]

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

post_creator(source_url, base_url, source_language, target_language, "publish")
~~~~

As principais diferenças em relação ao código anterior são:

    Adicion

continue

Continuando a explicação das principais diferenças em relação ao código anterior:

    Adicionei uma nova função create_gutenberg_block que recebe os parâmetros necessários para criar um bloco de conteúdo do Gutenberg (nome do bloco, atributos, blocos internos e conteúdo). Essa função retorna um dicionário que representa o bloco.

    Na seção de criação dos blocos de conteúdo, ao invés de usar a análise do HTML com BeautifulSoup, eu simplesmente crio um bloco de parágrafo com o conteúdo traduzido. Você pode adicionar mais condições nessa seção para criar outros tipos de blocos, como títulos, imagens, listas, etc.

    No payload do POST request, eu uso json.dumps(content_blocks) para enviar o conteúdo no formato esperado pelo Gutenberg, com a estrutura de blocos.

Essa abordagem é mais simples e direta do que a versão anterior, pois não requer a análise do HTML com BeautifulSoup. Ela também permite uma maior flexibilidade na criação dos blocos de conteúdo, já que você pode adicionar novos tipos de blocos conforme necessário.

Observe que, se você quiser adicionar suporte para outros tipos de blocos (como Imagem, Lista, Citação, etc.), basta adicionar mais chamadas à função create_gutenberg_block na seção de criação dos blocos de conteúdo, com os atributos e conteúdo apropriados.







- Criando a v8
/home/fernando/cursos/python/wordpress-blog-post-with-python/testes/script-v8.py

- Testando
não funcionou

- Trouxe 1 bloco com o titulo, que não é bloco Gutemberg
e um bloco com o html etc





- Criando a v9
/home/fernando/cursos/python/wordpress-blog-post-with-python/testes/script-v9.py

nada ocorreu


(ambiente-virtual-novo) root@1c297bab36f0:/teste# python3 script.py
(ambiente-virtual-novo) root@1c297bab36f0:/teste#



# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## Dia 01/02/2025

- Testando
cria o post ok
porém:
1. O "Table of Contents" vem como editor clássico no post traduzido.
2. Capa é perdida.
3. HREFLANG, idioma vem igual ao idioma do post original, necessário ajustar lógica do script para ajustar o HREFLANG para o TARGET_LANGUAGE.
4. Paragrafos vem em editor clássico, precisam vir em Blocos.


# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## PENDENTE

- Testando
    1. O "Table of Contents" vem como editor clássico no post traduzido.
    2. Capa é perdida.
    3. HREFLANG, idioma vem igual ao idioma do post original, necessário ajustar lógica do script para ajustar o HREFLANG para o TARGET_LANGUAGE.
    4. Paragrafos vem em editor clássico, precisam vir em Blocos.

- OBS
  Lidar com Blocos pode demandar conhecimento avançado em Javascript, NodeJS, etc.
  Pode ser uma opção aceitar o formato atual, converter para blocos manualmente e ajustar o que vem errado, como: TOC, Listas, Imagens(vem errado o ALT e a amostra no editor, mas imagem aparece no post)

- Avaliar se vale a pena tentar com BeautifulSoup.
- Criar uma v2 com   HREFLANG do Post em ingles????
- Criar variável para pegar o ID do Post via variável cadastrada no .env

- V2 com GPT e/ou Copilot
ver como fazer:
    Converter post para Editor em Blocos ao invés do Editor Clássico.
    Ajustar HREFLANG do Post.
    Tratar para que o TOC(Table of Contents) venha corretamente.
Ver idéia: <https://automatevalue.com/blog/wordpress-blocks-post-using-the-rest-api/>
<https://jeremyrichardson.dev/blog/parsing-a-raw-wordpress-post-with-blocks>
<https://community.zapier.com/how-do-i-3/how-to-create-wordpress-post-using-block-editor-instead-of-classic-editor-in-zapier-28770>
<https://developer.wordpress.org/rest-api/reference/posts/#create-a-post>
possível solução:
<https://myshittycode.com/2023/01/03/wordpress-creating-gutenberg-block-compatible-posts-using-rest-api/>

**MELHORIAS, V2** - Fazer que o post traduzido seja criado com Editor Wordpress avançado, ao invés do editor clássico. Que algumas formatações não se percam.
**MELHORIAS, v3**, Ver como pegar no JSON a capa do Post, imagem destaque, definir categoria, linguagem,  etc. Verificar demais melhoriais que é possível realizar.
- MELHORIAS, Ver como pegar no JSON a capa do Post, imagem destaque, definir categoria, linguagem,  etc. Verificar demais melhoriais que é possível realizar.
- Testar com o Blog devopsmind.
- Fixar versões contidas no "requirements.txt", definir versões exatas.
- Criar Dockerfile e docker-compose, posteriormente. Avaliar melhores práticas.
- Ver forma de acionar fácil o script para um blog e post especifico, chamar uma CLI que vai perguntando os dados desejados. Usar Makefile +CLI??? Variar ambiente virtual??? Avaliar as opções.
- Ver como obter os JSON de blogs do exterior e automatizar o processo de criar um post, com base na página do exterior, adicionar menções ao DevOps Mind no cabeçalho.
- Adicionar try, exception, logs de erros.
- Testar combo "Fedora 40 + PyTorch" , <https://www.tudocelular.com/tech/noticias/n219464/fedora-linux-40-beta-lancado-gnome-46-ia.html>


### N8N + IA

- Opç






# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## Dia 02/02/2025

como melhorar este código, para que O "Table of Contents" não venha como editor clássico no post traduzido, mas sim em blocos Gutenberg ?

não só o table of contents, o resto do conteudo do post traduzido fica com editor classico.
quero que todo o post inteiro seja convertido para blocos gutenberg logo na tradução, para nao precisar modificar para blocos gutenberg, como fazer?


- Criando v10
/home/fernando/cursos/python/wordpress-blog-post-with-python/testes/script-v10.py

- Testando


ERRO

~~~~bash
 python3 script.py
Traceback (most recent call last):
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/urllib3/connection.py", line 198, in _new_conn
    sock = connection.create_connection(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/urllib3/util/connection.py", line 60, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/socket.py", line 976, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
socket.gaierror: [Errno -3] Temporary failure in name resolution

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/urllib3/connectionpool.py", line 787, in urlopen
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/urllib3/connectionpool.py", line 488, in _make_request
    raise new_e
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/urllib3/connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/urllib3/connectionpool.py", line 1093, in _validate_conn
    conn.connect()
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/urllib3/connection.py", line 704, in connect
    self.sock = sock = self._new_conn()
                       ^^^^^^^^^^^^^^^^
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/urllib3/connection.py", line 205, in _new_conn
    raise NameResolutionError(self.host, self, e) from e
urllib3.exceptions.NameResolutionError: <urllib3.connection.HTTPSConnection object at 0x7f3d2d379eb0>: Failed to resolve 'palegreen-hornet-335449.hostingersite.com' ([Errno -3] Temporary failure in name resolution)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/requests/adapters.py", line 667, in send
    resp = conn.urlopen(
           ^^^^^^^^^^^^^
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/urllib3/connectionpool.py", line 841, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/urllib3/util/retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='palegreen-hornet-335449.hostingersite.com', port=443): Max retries exceeded with url: /wp-json/wp/v2/posts/3282 (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x7f3d2d379eb0>: Failed to resolve 'palegreen-hornet-335449.hostingersite.com' ([Errno -3] Temporary failure in name resolution)"))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/fernando/cursos/python/wordpress-blog-post-with-python/script.py", line 108, in <module>
    post_creator(source_url, base_url, source_language, target_language, "publish")
  File "/home/fernando/cursos/python/wordpress-blog-post-with-python/script.py", line 19, in post_creator
    response_API = requests.get(sourceURL)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/requests/api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/requests/api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/requests/sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/requests/sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/requests/adapters.py", line 700, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='palegreen-hornet-335449.hostingersite.com', port=443): Max retries exceeded with url: /wp-json/wp/v2/posts/3282 (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x7f3d2d379eb0>: Failed to resolve 'palegreen-hornet-335449.hostingersite.com' ([Errno -3] Temporary failure in name resolution)"))
~~~~



- Utilizando o v4 que é OK, deu mesmo erro.
- Utilizando o v4 que é OK, deu mesmo erro.


- Resolução parece ok


> dig palegreen-hornet-335449.hostingersite.com

; <<>> DiG 9.18.30-0ubuntu0.22.04.2-Ubuntu <<>> palegreen-hornet-335449.hostingersite.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 42781
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;palegreen-hornet-335449.hostingersite.com. IN A

;; ANSWER SECTION:
palegreen-hornet-335449.hostingersite.com. 3507 IN CNAME free.cdn.hstgr.net.
free.cdn.hstgr.net.     60      IN      A       89.116.213.130

;; Query time: 29 msec
;; SERVER: 8.8.8.8#53(8.8.8.8) (UDP)
;; WHEN: Sun Feb 02 17:25:35 -03 2025
;; MSG SIZE  rcvd: 118

> date
Sun Feb  2 17:25:40 -03 2025




git status
git add .
git commit -m "Wordpress with Python."
git push
git status









Ao tentar executar script em python ocorre o erro abaixo
porém antes estava ok

o que pode ser?
o dig indica tudo certo para resolução de nomes

ERRO:

~~~~bash
 python3 script.py
Traceback (most recent call last):
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/urllib3/connection.py", line 198, in _new_conn
    sock = connection.create_connection(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/urllib3/util/connection.py", line 60, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/socket.py", line 976, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
socket.gaierror: [Errno -3] Temporary failure in name resolution

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/fernando/cursos/python/wordpress-blog-post-with-python/script.py", line 108, in <module>
    post_creator(source_url, base_url, source_language, target_language, "publish")
  File "/home/fernando/cursos/python/wordpress-blog-post-with-python/script.py", line 19, in post_creator
    response_API = requests.get(sourceURL)
                   ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/requests/api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/requests/api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/requests/sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/requests/sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/fernando/.asdf/installs/python/3.12.6/lib/python3.12/site-packages/requests/adapters.py", line 700, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='palegreen-hornet-335449.hostingersite.com', port=443): Max retries exceeded with url: /wp-json/wp/v2/posts/3282 (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x7f3d2d379eb0>: Failed to resolve 'palegreen-hornet-335449.hostingersite.com' ([Errno -3] Temporary failure in name resolution)"))
~~~~


> dig palegreen-hornet-335449.hostingersite.com

; <<>> DiG 9.18.30-0ubuntu0.22.04.2-Ubuntu <<>> palegreen-hornet-335449.hostingersite.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 42781
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;palegreen-hornet-335449.hostingersite.com. IN A

;; ANSWER SECTION:
palegreen-hornet-335449.hostingersite.com. 3507 IN CNAME free.cdn.hstgr.net.
free.cdn.hstgr.net.     60      IN      A       89.116.213.130

;; Query time: 29 msec
;; SERVER: 8.8.8.8#53(8.8.8.8) (UDP)
;; WHEN: Sun Feb 02 17:25:35 -03 2025
;; MSG SIZE  rcvd: 118

> date
Sun Feb  2 17:25:40 -03 2025



- TSHOOT


> curl -I https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/posts/3282
curl: (6) Could not resolve host: palegreen-hornet-335449.hostingersite.com
> nslookup palegreen-hornet-335449.hostingersite.com
;; communications error to 8.8.8.8#53: timed out
;; communications error to 8.8.8.8#53: timed out
^C
> nslookup google.com
;; communications error to 8.8.8.8#53: timed out
;; communications error to 8.8.8.8#53: timed out
^C




- OK:

> cat /etc/resolv.conf
nameserver 8.8.8.8
>
>
>
> nslookup google.com
Server:         8.8.8.8
Address:        8.8.8.8#53

Non-authoritative answer:
Name:   google.com
Address: 172.217.30.46
Name:   google.com
Address: 2800:3f0:4001:806::200e




> curl -I https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/posts/3282
curl: (35) error:0A000438:SSL routines::tlsv1 alert internal error










> openssl s_client -connect palegreen-hornet-335449.hostingersite.com:443 -showcerts
CONNECTED(00000003)
4047B745857F0000:error:0A000438:SSL routines:ssl3_read_bytes:tlsv1 alert internal error:../ssl/record/rec_layer_s3.c:1593:SSL alert number 80
---
no peer certificate available
---
No client certificate CA names sent
---
SSL handshake has read 7 bytes and written 343 bytes
Verification: OK
---
New, (NONE), Cipher is (NONE)
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 0 (ok)
---




O erro **`tlsv1 alert internal error`** e a mensagem **`no peer certificate available`** indicam que o servidor **não está respondendo corretamente às conexões SSL**.  

Isso significa que o problema está no servidor do **Hostinger** (ou no CDN que ele usa), e **não na sua máquina**.

---

## 🔍 **Possíveis causas e soluções**

### 1️⃣ **Servidor pode estar com problemas no SSL**  
- Como o erro ocorre no **handshake**, pode ser um problema no certificado SSL.  
- **Se o site for seu**, acesse o painel da Hostinger e tente **renovar/reinstalar o SSL**.

✅ **Solução:**  
No painel da Hostinger:
- Vá até **Hospedagem > Domínios > SSL**
- Verifique o status e tente renovar o certificado.

---

### 2️⃣ **Cloudflare pode estar bloqueando**  
Se o domínio estiver usando **Cloudflare**, o erro pode ser causado por um problema no modo SSL.

✅ **Solução:**  
Acesse o painel do **Cloudflare** e altere o modo SSL para:
- **"Full"** (se estiver em "Full (Strict)")
- **"Flexible"** (para testar)

---

### 3️⃣ **CDN ou Firewall bloqueando**  
O domínio **palegreen-hornet-335449.hostingersite.com** resolve para um **CDN da Hostinger**, que pode estar bloqueando seu IP.

✅ **Solução:**  
Tente **acessar de outra rede** (por exemplo, um hotspot do celular).  
Se funcionar, a Hostinger pode estar bloqueando sua rede.

---

### 4️⃣ **Problema no Certificado SSL do CDN**  
Se o site estiver atrás de um **CDN da Hostinger**, pode haver um problema com a comunicação entre o CDN e o servidor.

✅ **Solução:**  
- Se for seu site, tente desativar o CDN temporariamente no painel da Hostinger.  
- Se não for seu site, o problema é do **Hostinger/CDN**, e você precisará esperar ou entrar em contato com o suporte.

---

### 5️⃣ **Testar com HTTP (sem SSL)**  
Se o erro for no SSL, veja se o servidor responde via **HTTP**:
```bash
curl -I http://palegreen-hornet-335449.hostingersite.com
```
Se funcionar, mas o **HTTPS continuar falhando**, o problema está no certificado SSL.

---

## 🚀 **Conclusão**  
🔴 **O problema não está no seu Python, nem no seu `curl`.**  
🔴 **O erro está no SSL do servidor da Hostinger ou no CDN.**  

✅ **Se o site for seu:**  
1. **Renove/reinstale o SSL** no painel da Hostinger.  
2. **Teste sem CDN** ou **mude as configurações SSL no Cloudflare**.  
3. **Entre em contato com o suporte da Hostinger** se o problema persistir.  

✅ **Se o site não for seu:**  
- **O servidor está com problemas** e você terá que esperar ou entrar em contato com o dono.  

---

Me avise se precisar de mais ajuda! 🚀





- No Sandbox do lab ta ok:


student-node ~ ➜  nslookup palegreen-hornet-335449.hostingersite.com
Server:         10.96.0.10
Address:        10.96.0.10#53

Non-authoritative answer:
palegreen-hornet-335449.hostingersite.com       canonical name = free.cdn.hstgr.net.
Name:   free.cdn.hstgr.net
Address: 77.37.42.32
Name:   free.cdn.hstgr.net
Address: 2a02:4780:4e:c278:35b9:b924:f9dc:b21d


student-node ~ ➜  curl -I https://palegreen-hornet-335449.hostingersite.com/wp-json/wp/v2/posts/3282
HTTP/2 200 
date: Sun, 02 Feb 2025 21:21:06 GMT
content-type: application/json; charset=UTF-8
vary: Accept-Encoding
x-powered-by: PHP/8.1.27
x-robots-tag: noindex
x-content-type-options: nosniff
access-control-expose-headers: X-WP-Total, X-WP-TotalPages, Link
access-control-allow-headers: Authorization, X-WP-Nonce, Content-Disposition, Content-MD5, Content-Type
link: <https://palegreen-hornet-335449.hostingersite.com/docker-sre-e-devops-uma-abordagem-integrada-para-confiabilidade-e-eficiencia/>; rel="alternate"; type=text/html
allow: GET
platform: hostinger
panel: hpanel
content-security-policy: upgrade-insecure-requests
server: hcdn
x-hcdn-request-id: d39c3e17c652726d88d4bf773f1383e3-bos-edge4
x-hcdn-cache-status: DYNAMIC
x-hcdn-upstream-rt: 0.778





- Segue erro:


    raise SSLError(e, request=request)
requests.exceptions.SSLError: HTTPSConnectionPool(host='palegreen-hornet-335449.hostingersite.com', port=443): Max retries exceeded with url: /wp-json/wp/v2/posts/3282 (Caused by SSLError(SSLError(1, '[SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:1000)')))


## PENDENTE:
- TSHOOT do WSL2 e DNS, SSL





# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## Dia 03/02/2025


- Hoje estava ok o WSL2
sem erros de DNS



- Testando script-v10
/home/fernando/cursos/python/wordpress-blog-post-with-python/testes/script-v10.py

- Script sem erros ao executar
porém o post traduzido ficou:
1. Num bloco inteiro, com editor clássico.
2. Diversas linhas contendo informações aleatórias. Como "[{"blockName": "core/table-of-contents", "attrs": {}, "innerBlocks": [], "innerHTML": ""}, {"blockName": "core/paragraph", "attrs": {}, "innerBlocks": [], "innerHTML"" , etc, além de "\n\n\n\n"

Preciso que o código não gere um post num bloco único
Não pode ser usado editor clássico do wordpress
traduzir independente do tipo de Bloco do WordPress na origem, pensando que ao final da tradução cada Bloco do WordPress fique no padrão utilizado pelo editor Gutenberg na origem seja um bloco Gutenberg no destino(post traduzido).




Hoje eu possuo um script em Python que traduz posts do Wordpress, porém ele tem algumas limitações:

    1. O "Table of Contents" vem como editor clássico no post traduzido.
    2. Capa é perdida.
    3. HREFLANG, idioma vem igual ao idioma do post original, necessário ajustar lógica do script para ajustar o HREFLANG com base na variavel TARGET_LANGUAGE.
    4. Paragrafos vem em editor clássico, não vem em Blocos Wordpress no padrão Gutenberg.

Utilizar o n8n para traduzir os posts Wordpress pode ser uma opção? Como seria feito?












https://github.com/n8n-io/self-hosted-ai-starter-kit

Installation
Cloning the Repository

git clone https://github.com/n8n-io/self-hosted-ai-starter-kit.git
cd self-hosted-ai-starter-kit

Running n8n using Docker Compose
For Nvidia GPU users

git clone https://github.com/n8n-io/self-hosted-ai-starter-kit.git
cd self-hosted-ai-starter-kit
docker compose --profile gpu-nvidia up


- Deu erro
reinstalando o Docker Desktop

- Executando novamente
docker compose --profile gpu-nvidia up


> docker ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS                    PORTS                              NAMES
d47580122786   n8nio/n8n:latest       "tini -- /docker-ent…"   14 minutes ago   Up 14 minutes             0.0.0.0:5678->5678/tcp             n8n
41a2d1b5e62c   qdrant/qdrant          "./entrypoint.sh"        14 minutes ago   Up 14 minutes             0.0.0.0:6333->6333/tcp, 6334/tcp   qdrant
fce35e5c3cc0   postgres:16-alpine     "docker-entrypoint.s…"   14 minutes ago   Up 14 minutes (healthy)   5432/tcp                           self-hosted-ai-starter-kit-postgres-1
db2914f53fd4   ollama/ollama:latest   "/bin/ollama serve"      14 minutes ago   Up 14 minutes             0.0.0.0:11434->11434/tcp           ollama

 ~           




ótimo video:
https://www.youtube.com/watch?v=tQLpKlmlmak






- Como fazer via n8n

### DeepSeek

Sim, utilizar o n8n para traduzir posts do WordPress pode ser uma opção viável e eficiente, especialmente para automatizar o processo e resolver as limitações que você mencionou. O n8n é uma ferramenta de automação de fluxo de trabalho que permite integrar diferentes serviços e APIs, o que pode ser útil para manipular posts do WordPress, traduzir conteúdo e ajustar metadados como HREFLANG.

Aqui está um exemplo de como você poderia configurar um fluxo de trabalho no n8n para traduzir posts do WordPress:

### Passos para Configurar o Fluxo de Trabalho no n8n:

1. **Obter Posts do WordPress:**
   - Use o nó "HTTP Request" ou "WordPress" (se disponível) para buscar os posts do WordPress que precisam ser traduzidos.
   - Configure o nó para acessar a API REST do WordPress e buscar os posts.

2. **Extrair Conteúdo do Post:**
   - Use nós como "Function" ou "Set" para extrair o conteúdo do post, como título, corpo, metadados, etc.

3. **Traduzir o Conteúdo:**
   - Use um serviço de tradução como o Google Translate, DeepL, ou outro via API.
   - Configure um nó "HTTP Request" para enviar o conteúdo para a API de tradução e receber o texto traduzido.

4. **Ajustar Metadados (HREFLANG):**
   - Use um nó "Function" para ajustar o metadado HREFLANG com base na variável `TARGET_LANGUAGE`.
   - Atualize os metadados do post traduzido para refletir o idioma correto.

5. **Converter Conteúdo para Blocos Gutenberg:**
   - Use um nó "Function" para converter o conteúdo traduzido para o formato de blocos Gutenberg.
   - Isso pode envolver a manipulação de strings para adicionar os blocos necessários.

6. **Manter a Capa do Post:**
   - Extraia a URL da imagem de capa do post original.
   - Use um nó "HTTP Request" para fazer o upload da imagem de capa no WordPress traduzido.
   - Associe a imagem de capa ao novo post traduzido.

7. **Publicar o Post Traduzido:**
   - Use o nó "HTTP Request" ou "WordPress" para criar um novo post no WordPress com o conteúdo traduzido e os metadados ajustados.
   - Certifique-se de que o novo post seja publicado no idioma correto.

### Exemplo de Fluxo de Trabalho no n8n:

1. **Trigger:** Inicie o fluxo de trabalho manualmente ou agende-o para rodar automaticamente.
2. **HTTP Request (WordPress API):** Busque os posts que precisam ser traduzidos.
3. **Function Node:** Extraia o conteúdo do post, incluindo título, corpo, metadados e URL da imagem de capa.
4. **HTTP Request (API de Tradução):** Envie o conteúdo para tradução.
5. **Function Node:** Ajuste o metadado HREFLANG com base na variável `TARGET_LANGUAGE`.
6. **Function Node:** Converta o conteúdo traduzido para o formato de blocos Gutenberg.
7. **HTTP Request (WordPress API):** Faça o upload da imagem de capa e associe ao novo post.
8. **HTTP Request (WordPress API):** Crie e publique o novo post traduzido.

### Considerações Finais:

- **Autenticação:** Certifique-se de configurar a autenticação corretamente para acessar a API do WordPress e a API de tradução.
- **Tratamento de Erros:** Adicione nós para tratar erros, como falhas na tradução ou na publicação do post.
- **Testes:** Teste o fluxo de trabalho com alguns posts antes de colocá-lo em produção para garantir que tudo funcione como esperado.

Utilizando o n8n, você pode automatizar todo o processo de tradução e publicação de posts no WordPress, resolvendo as limitações que você mencionou e melhorando a eficiência do seu workflow.






--- 


README:
<https://github.com/n8n-io/self-hosted-ai-starter-kit/blob/main/README.md>

## 👓 Recommended reading

n8n is full of useful content for getting started quickly with its AI concepts
and nodes. If you run into an issue, go to [support](#support).

- [AI agents for developers: from theory to practice with n8n](https://blog.n8n.io/ai-agents/)
- [Tutorial: Build an AI workflow in n8n](https://docs.n8n.io/advanced-ai/intro-tutorial/)
- [Langchain Concepts in n8n](https://docs.n8n.io/advanced-ai/langchain/langchain-n8n/)
- [Demonstration of key differences between agents and chains](https://docs.n8n.io/advanced-ai/examples/agent-chain-comparison/)
- [What are vector databases?](https://docs.n8n.io/advanced-ai/examples/understand-vector-databases/)

## 🎥 Video walkthrough

- [Installing and using Local AI for n8n](https://www.youtube.com/watch?v=xz_X2N-hPg0)

## 🛍️ More AI templates

For more AI workflow ideas, visit the [**official n8n AI template
gallery**](https://n8n.io/workflows/?categories=AI). From each workflow,
select the **Use workflow** button to automatically import the workflow into
your local n8n instance.

### Learn AI key concepts

- [AI Agent Chat](https://n8n.io/workflows/1954-ai-agent-chat/)
- [AI chat with any data source (using the n8n workflow too)](https://n8n.io/workflows/2026-ai-chat-with-any-data-source-using-the-n8n-workflow-tool/)
- [Chat with OpenAI Assistant (by adding a memory)](https://n8n.io/workflows/2098-chat-with-openai-assistant-by-adding-a-memory/)
- [Use an open-source LLM (via Hugging Face)](https://n8n.io/workflows/1980-use-an-open-source-llm-via-huggingface/)
- [Chat with PDF docs using AI (quoting sources)](https://n8n.io/workflows/2165-chat-with-pdf-docs-using-ai-quoting-sources/)
- [AI agent that can scrape webpages](https://n8n.io/workflows/2006-ai-agent-that-can-scrape-webpages/)

### Local AI templates

- [Tax Code Assistant](https://n8n.io/workflows/2341-build-a-tax-code-assistant-with-qdrant-mistralai-and-openai/)
- [Breakdown Documents into Study Notes with MistralAI and Qdrant](https://n8n.io/workflows/2339-breakdown-documents-into-study-notes-using-templating-mistralai-and-qdrant/)
- [Financial Documents Assistant using Qdrant and](https://n8n.io/workflows/2335-build-a-financial-documents-assistant-using-qdrant-and-mistralai/) [Mistral.ai](http://mistral.ai/)
- [Recipe Recommendations with Qdrant and Mistral](https://n8n.io/workflows/2333-recipe-recommendations-with-qdrant-and-mistral/)

## Tips & tricks

### Accessing local files

The self-hosted AI starter kit will create a shared folder (by default,
located in the same directory) which is mounted to the n8n container and
allows n8n to access files on disk. This folder within the n8n container is
located at `/data/shared` -- this is the path you’ll need to use in nodes that
interact with the local filesystem.

**Nodes that interact with the local filesystem**

- [Read/Write Files from Disk](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.filesreadwrite/)
- [Local File Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger/)
- [Execute Command](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/)












Para extrair o conteúdo do post, incluindo título, corpo, metadados e URL da imagem de capa, você pode usar um **Function Node** no n8n. Esse nó permite escrever código JavaScript personalizado para manipular os dados que passam pelo fluxo de trabalho.

Aqui está um exemplo de como você pode configurar o **Function Node** para extrair essas informações:

---

### Passo a Passo:

1. **Adicione um Function Node:**
   - No n8n, arraste e solte um nó **Function** no seu fluxo de trabalho.
   - Conecte-o ao nó anterior (por exemplo, um nó que busca os posts via API do WordPress).

2. **Escreva o Código JavaScript:**
   - No **Function Node**, você pode escrever código JavaScript para processar os dados recebidos.
   - Abaixo está um exemplo de código para extrair o título, corpo, metadados e URL da imagem de capa de um post do WordPress:

```javascript
// O n8n passa os dados recebidos em um array chamado `items`
return items.map(item => {
  // Extrair o título do post
  const title = item.json.title?.rendered || 'Sem título';

  // Extrair o corpo do post (conteúdo)
  const content = item.json.content?.rendered || 'Sem conteúdo';

  // Extrair metadados (exemplo: HREFLANG, idioma, etc.)
  const metadata = item.json.meta || {};

  // Extrair a URL da imagem de capa (featured image)
  const featuredImageUrl = item.json.featured_media_url || item.json._links?.['wp:featuredmedia']?.[0]?.href || 'Sem imagem de capa';

  // Retornar os dados extraídos
  return {
    json: {
      title,
      content,
      metadata,
      featuredImageUrl,
      // Você pode adicionar outros campos aqui, se necessário
    }
  };
});
```

---

### Explicação do Código:

1. **`items.map(item => { ... })`:**
   - O n8n passa os dados recebidos em um array chamado `items`. O método `map` é usado para processar cada item individualmente.

2. **Extrair o Título:**
   - O título do post geralmente está no campo `title.rendered` da resposta da API do WordPress.

3. **Extrair o Corpo do Post:**
   - O conteúdo do post está no campo `content.rendered`.

4. **Extrair Metadados:**
   - Os metadados do post estão no campo `meta`. Dependendo da configuração do WordPress, isso pode incluir campos personalizados, como HREFLANG.

5. **Extrair a URL da Imagem de Capa:**
   - A URL da imagem de capa pode estar no campo `featured_media_url` ou no campo `_links['wp:featuredmedia'][0].href` (dependendo da resposta da API do WordPress).

6. **Retornar os Dados:**
   - O n8n espera que o **Function Node** retorne um array de objetos com a estrutura `{ json: { ... } }`. Aqui, retornamos os dados extraídos nesse formato.

---

### Exemplo de Saída:

Se o post do WordPress tiver os seguintes dados:

```json
{
  "title": {
    "rendered": "Meu Post"
  },
  "content": {
    "rendered": "<p>Este é o conteúdo do post.</p>"
  },
  "meta": {
    "hreflang": "pt-BR"
  },
  "featured_media_url": "https://exemplo.com/imagem.jpg"
}
```

O **Function Node** retornará:

```json
{
  "json": {
    "title": "Meu Post",
    "content": "<p>Este é o conteúdo do post.</p>",
    "metadata": {
      "hreflang": "pt-BR"
    },
    "featuredImageUrl": "https://exemplo.com/imagem.jpg"
  }
}
```

---

### Dicas:

1. **Verifique a Estrutura da API do WordPress:**
   - A estrutura da resposta da API do WordPress pode variar dependendo da configuração do seu site. Use o nó **HTTP Request** para testar a API e verificar como os dados são retornados.

2. **Trate Campos Opcionais:**
   - Use operadores como `?.` para evitar erros caso algum campo não exista na resposta.

3. **Adicione Mais Campos:**
   - Se precisar de mais informações, como tags, categorias ou autor, você pode adicionar mais campos ao código.

4. **Teste o Function Node:**
   - Execute o fluxo de trabalho e verifique se os dados estão sendo extraídos corretamente.

---

Com isso, você terá um **Function Node** que extrai o título, conteúdo, metadados e URL da imagem de capa de um post do WordPress, pronto para ser usado no restante do seu fluxo de trabalho no n8n!






Se você não tem acesso a uma API de tradução paga, como Google Translate ou DeepL, e deseja traduzir o conteúdo obtido via **Function Node** usando uma solução local como o **Ollama**, isso é perfeitamente possível! O Ollama é uma ferramenta que permite rodar modelos de linguagem grandes (LLMs) localmente, como o **LLaMA**, **Mistral**, ou outros modelos que podem ser usados para tradução.

Aqui está um passo a passo de como você pode integrar o Ollama ao n8n para traduzir o conteúdo:

---

### Passo 1: Configurar o Ollama Localmente

1. **Instale o Ollama:**
   - Siga as instruções de instalação do Ollama no seu sistema operacional. Você pode encontrar o guia oficial no repositório do Ollama: [Ollama GitHub](https://github.com/jmorganca/ollama).

2. **Baixe um Modelo de Tradução:**
   - O Ollama suporta vários modelos. Para tradução, você pode usar modelos como o **LLaMA**, **Mistral**, ou outros que sejam adequados para tarefas de tradução.
   - Por exemplo, para baixar o modelo Mistral, use o comando:
     ```bash
     ollama pull mistral
     ```

3. **Teste o Ollama Localmente:**
   - Certifique-se de que o Ollama está funcionando corretamente. Você pode testar enviando uma solicitação de tradução via linha de comando ou usando uma ferramenta como o `curl`:
     ```bash
     curl http://localhost:11434/api/generate -d '{
       "model": "mistral",
       "prompt": "Traduza para o inglês: Olá, como você está?",
       "stream": false
     }'
     ```

---

### Passo 2: Configurar o n8n para Usar o Ollama

1. **Adicione um Nó HTTP Request no n8n:**
   - O Ollama expõe uma API local na porta `11434`. Você pode usar o nó **HTTP Request** no n8n para enviar o conteúdo a ser traduzido para o Ollama.

2. **Configure o Nó HTTP Request:**
   - **URL:** `http://localhost:11434/api/generate`
   - **Método:** POST
   - **Headers:** Adicione um cabeçalho `Content-Type: application/json`.
   - **Body (JSON):**
     ```json
     {
       "model": "mistral",
       "prompt": "Traduza para o {{$node["Function"].json["targetLanguage"]}}: {{$node["Function"].json["content"]}}",
       "stream": false
     }
     ```
     - Substitua `{{$node["Function"].json["targetLanguage"]}}` pelo idioma de destino (ex: `inglês`, `espanhol`, etc.).
     - Substitua `{{$node["Function"].json["content"]}}` pelo conteúdo que você extraiu no **Function Node**.

3. **Processe a Resposta do Ollama:**
   - O Ollama retornará a tradução no campo `response` da resposta JSON.
   - Use um **Function Node** ou **Set Node** para extrair o texto traduzido e adicioná-lo ao fluxo de trabalho.

---

### Passo 3: Exemplo de Fluxo de Trabalho no n8n

Aqui está um exemplo de como o fluxo de trabalho pode ser estruturado:

1. **Function Node:**
   - Extraia o conteúdo do post (título, corpo, etc.) e defina o idioma de destino (`targetLanguage`).

2. **HTTP Request Node:**
   - Envie o conteúdo para o Ollama para tradução.

3. **Function Node (Pós-Tradução):**
   - Extraia o texto traduzido da resposta do Ollama.

4. **HTTP Request Node (WordPress API):**
   - Use o conteúdo traduzido para criar um novo post no WordPress.

---

### Exemplo de Código no Function Node (Pré-Tradução):

```javascript
// Extrair conteúdo e definir idioma de destino
return items.map(item => {
  const content = item.json.content || 'Sem conteúdo';
  const targetLanguage = 'inglês'; // Defina o idioma de destino aqui

  return {
    json: {
      content,
      targetLanguage
    }
  };
});
```

---

### Exemplo de Código no Function Node (Pós-Tradução):

```javascript
// Extrair a tradução da resposta do Ollama
return items.map(item => {
  const translatedText = item.json.response || 'Tradução falhou';

  return {
    json: {
      translatedText
    }
  };
});
```

---

### Passo 4: Executar e Testar

1. **Execute o Fluxo de Trabalho:**
   - Certifique-se de que o Ollama está rodando localmente e que o n8n está configurado corretamente para se comunicar com ele.

2. **Verifique os Resultados:**
   - Após a execução, verifique se o conteúdo foi traduzido corretamente e se o novo post foi criado no WordPress.

---

### Considerações Finais:

- **Desempenho:** Traduzir conteúdo localmente com Ollama pode ser mais lento do que usar uma API de tradução dedicada, dependendo do hardware disponível.
- **Qualidade da Tradução:** A qualidade da tradução depende do modelo usado. Experimente diferentes modelos para obter os melhores resultados.
- **Segurança:** Como o Ollama roda localmente, seus dados não são enviados para servidores externos, o que é uma vantagem em termos de privacidade.

Com essa configuração, você pode traduzir conteúdo do WordPress usando o Ollama localmente, sem depender de APIs de tradução externas! 🚀







- Testando Endpoint do Ollama local:

> curl http://localhost:11434/api/generate -d '{
  "model": "llama",
  "prompt": "Traduza para o inglês: Olá, como você está?",
  "stream": false
}'
{"error":"model 'llama' not found"}%
> ollama pull mistral
pulling manifest
pulling ff82381e2bea... 100% ▕████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏ 4.1 GB
pulling 43070e2d4e53... 100% ▕████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏  11 KB
pulling 491dfa501e59... 100% ▕████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏  801 B
pulling ed11eda7790d... 100% ▕████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏   30 B
pulling 42347cd80dc8... 100% ▕████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏  485 B
verifying sha256 digest
writing manifest
success
> curl http://localhost:11434/api/generate -d '{
  "model": "mistral",
  "prompt": "Traduza para o inglês: Olá, como você está?",
  "stream": false
}'
{"model":"mistral","created_at":"2025-02-04T03:12:47.957345415Z","response":" Hello, how are you?","done":true,"done_reason":"stop","context":[3,29473,18349,29486,2934,3414,1057,4923,29482,17962,29515,7780,29588,29493,3886,8669,29644,11944,29572,4,1027,23325,29493,1678,1228,1136,29572],"total_duration":4488770212,"load_duration":3503574739,"prompt_eval_count":22,"prompt_eval_duration":835000000,"eval_count":7,"eval_duration":146000000}%

 ~                                                   


- Após baixar mistral, ficou ok o curl para traduzir





No n8n, você pode acessar os dados de nós anteriores usando **expressões**. Essas expressões permitem referenciar valores de outros nós no fluxo de trabalho. Para substituir `{{$node["Function"].json["content"]}}` pelo conteúdo extraído no **Function Node**, siga os passos abaixo:

---

### Passo 1: Certifique-se de que o Function Node Retorna o Conteúdo

No **Function Node**, você deve retornar o conteúdo que deseja traduzir. Por exemplo:

```javascript
return items.map(item => {
  const content = item.json.content || 'Sem conteúdo'; // Extrai o conteúdo
  const targetLanguage = 'inglês'; // Define o idioma de destino

  return {
    json: {
      content, // Conteúdo a ser traduzido
      targetLanguage // Idioma de destino
    }
  };
});
```

Isso garante que o conteúdo esteja disponível para ser referenciado em nós subsequentes.

---

### Passo 2: Usar Expressões no HTTP Request Node

No nó **HTTP Request** que envia o conteúdo para o Ollama, você pode usar uma expressão para acessar o conteúdo retornado pelo **Function Node**.

1. **Abra o Nó HTTP Request:**
   - No campo **Body (JSON)**, você verá uma opção para usar expressões.

2. **Use a Expressão Correta:**
   - Para acessar o conteúdo do **Function Node**, use a seguinte expressão:
     ```plaintext
     {{$node["Function"].json["content"]}}
     ```
   - Para acessar o idioma de destino, use:
     ```plaintext
     {{$node["Function"].json["targetLanguage"]}}
     ```

3. **Exemplo de Configuração do Body (JSON):**
   ```json
   {
     "model": "mistral",
     "prompt": "Traduza para o {{$node["Function"].json["targetLanguage"]}}: {{$node["Function"].json["content"]}}",
     "stream": false
   }
   ```

   Aqui:
   - `{{$node["Function"].json["targetLanguage"]}}` será substituído pelo valor de `targetLanguage` retornado pelo **Function Node**.
   - `{{$node["Function"].json["content"]}}` será substituído pelo valor de `content` retornado pelo **Function Node**.

---

### Passo 3: Testar a Expressão

1. **Execute o Fluxo de Trabalho:**
   - Clique em **Execute Workflow** para testar o fluxo.

2. **Verifique o Body Enviado:**
   - Após a execução, abra o nó **HTTP Request** e verifique a aba **Request**.
   - Certifique-se de que o corpo da solicitação (Body) foi preenchido corretamente com o conteúdo e o idioma de destino.

   Exemplo de Body enviado:
   ```json
   {
     "model": "mistral",
     "prompt": "Traduza para o inglês: Este é o conteúdo do post.",
     "stream": false
   }
   ```

---

### Passo 4: Lidar com Erros

Se a expressão não funcionar corretamente:
1. **Verifique o Nome do Nó:**
   - Certifique-se de que o nome do nó no fluxo de trabalho corresponde ao usado na expressão. Por exemplo, se o nó se chama "Function 1", use:
     ```plaintext
     {{$node["Function 1"].json["content"]}}
     ```

2. **Verifique a Estrutura dos Dados:**
   - Use o **Debug Node** ou inspecione a saída do **Function Node** para garantir que os dados estejam no formato esperado.

3. **Teste Expressões Simples:**
   - Teste expressões simples, como `{{$node["Function"].json}}`, para verificar se os dados estão sendo passados corretamente.

---

### Exemplo Completo do Fluxo de Trabalho

1. **Function Node:**
   - Extrai o conteúdo e define o idioma de destino.

2. **HTTP Request Node:**
   - Envia o conteúdo para o Ollama usando expressões para preencher o Body.

3. **Function Node (Pós-Tradução):**
   - Extrai o texto traduzido da resposta do Ollama.

4. **HTTP Request Node (WordPress API):**
   - Cria um novo post no WordPress com o conteúdo traduzido.

---

### Dicas Finais:

- **Use o Debug Node:**
  - Adicione um nó **Debug** após o **Function Node** para visualizar os dados retornados e garantir que estão no formato correto.

- **Documentação do n8n:**
  - Consulte a [documentação oficial do n8n sobre expressões](https://docs.n8n.io/code-examples/expressions/) para mais exemplos e detalhes.

Com isso, você conseguirá substituir `{{$node["Function"].json["content"]}}` pelo conteúdo extraído no **Function Node** e enviá-lo para o Ollama para tradução! 🚀








- Tratar workflow
Problem in node ‘HTTP Request - para enviar ao Ollama local traduzir‘

JSON parameter needs to be valid JSON
{
  "nodes": [
    {
      "parameters": {
        "method": "POST",
        "url": "http://localhost:11434/api/generate",
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "Content-Type",
              "value": "application/json"
            }
          ]
        },
        "sendBody": true,
        "specifyBody": "json",
        "jsonBody": "{\n  \"model\": \"mistral\",\n  \"prompt\": \"Traduza para o {{$node[\"Function\"].json[\"inglês\"]}}: {{$node[\"Function\"].json[\"content\"]}}\",\n  \"stream\": false\n}",
        "options": {}
      },
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [
        820,
        -40
      ],
      "id": "1117b7f8-bc44-41d7-987c-cc3c809dfb3c",
      "name": "HTTP Request - para enviar ao Ollama local traduzir"
    }
  ],
  "connections": {},
  "pinData": {},
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "558d88703fb65b2d0e44613bc35916258b0f0bf983c5d4730c00c424b77ca36a"
  }
}




Problem in node ‘HTTP Request - para enviar ao Ollama local traduzir‘

JSON parameter needs to be valid JSON






# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## Dia 05/02/2025

num workflow do n8n, onde eu quero obter post do Wordpress, traduzir usando ollama local e postar o post traduzido no wordpress, como podem ser os steps?



código que usei no n8n para extrair dados do post wordpress:

````js
// O n8n passa os dados recebidos em um array chamado `items`
return items.map(item => {
  // Extrair o título do post
  const title = item.json.title?.rendered || 'Sem título';

  // Extrair o corpo do post (conteúdo)
  const content = item.json.content?.rendered || 'Sem conteúdo';

  // Extrair metadados (exemplo: HREFLANG, idioma, etc.)
  const metadata = item.json.meta || {};

  // Extrair a URL da imagem de capa (featured image)
  const featuredImageUrl = item.json.featured_media_url || item.json._links?.['wp:featuredmedia']?.[0]?.href || 'Sem imagem de capa';

  // Retornar os dados extraídos
  return {
    json: {
      title,
      content,
      metadata,
      featuredImageUrl,
      // Você pode adicionar outros campos aqui, se necessário
    }
  };
});
````

como eu crio um step do tipo HTTP Request para Traduzir o Conteúdo Usando o Ollama Local?




Codigo-Extrair-dados-do-post

{
  "model": "mistral",
  "prompt": "Traduza para o {{$node["Function"].json["inglês"]}}: {{$node["Function"].json["content"]}}",
  "stream": false
}


- Ajustando

{
  "model": "mistral",
  "prompt": "Traduza para o {{$node["Codigo-Extrair-dados-do-post"].json["targetLanguage"]}}: {{$node["Codigo-Extrair-dados-do-post"].json["content"]}}": Importante manter a estrutura do post sem afetar a formatação ou elementos do wordpress,
  "stream": false
}



JSON parameter needs to be valid JSON

Error details
Other info

Item Index

0

Node type

n8n-nodes-base.httpRequest

Node version

4.2 (Latest)

n8n version

1.76.2 (Self Hosted)

Time

05/02/2025, 11:38:04

Stack trace

NodeOperationError: JSON parameter needs to be valid JSON at ExecuteContext.execute (/usr/local/lib/node_modules/n8n/node_modules/n8n-nodes-base/dist/nodes/HttpRequest/V3/HttpRequestV3.node.js:207:39) at WorkflowExecute.runNode (/usr/local/lib/node_modules/n8n/node_modules/n8n-core/dist/execution-engine/workflow-execute.js:632:42) at /usr/local/lib/node_modules/n8n/node_modules/n8n-core/dist/execution-engine/workflow-execute.js:881:62 at processTicksAndRejections (node:internal/process/task_queues:95:5) at /usr/local/lib/node_modules/n8n/node_modules/n8n-core/dist/execution-engine/workflow-execute.js:1215:20



tentei 


{
  "model": "mistral",
  "prompt": "Traduza para o {{$node["Codigo-Extrair-dados-do-post"].json["targetLanguage"]}}: {{$node["Codigo-Extrair-dados-do-post"].json["content"]}}": Importante manter a estrutura do post sem afetar a formatação ou elementos do wordpress,
  "stream": false
}


deu erro
JSON parameter needs to be valid JSON





O erro "JSON parameter needs to be valid JSON" indica que o JSON que você está tentando enviar não é válido. No seu caso, há um problema de sintaxe no JSON. Vamos corrigir isso.

Problemas Identificados
Erro de Sintaxe: Há um : extra após a expressão {{$node["Codigo-Extrair-dados-do-post"].json["content"]}}.
Aspas: Certifique-se de que todas as aspas estejam corretamente fechadas.

JSON Corrigido:

{
  "model": "mistral",
  "prompt": "Traduza para o {{$node["Codigo-Extrair-dados-do-post"].json["targetLanguage"]}}: {{$node["Codigo-Extrair-dados-do-post"].json["content"]}}. Importante manter a estrutura do post sem afetar a formatação ou elementos do wordpress.",
  "stream": false
}




JSON parameter needs to be valid JSON

Error details
Other info

Item Index

0

Node type

n8n-nodes-base.httpRequest

Node version

4.2 (Latest)

n8n version

1.76.2 (Self Hosted)

Time

05/02/2025, 11:39:46

Stack trace

NodeOperationError: JSON parameter needs to be valid JSON at ExecuteContext.execute (/usr/local/lib/node_modules/n8n/node_modules/n8n-nodes-base/dist/nodes/HttpRequest/V3/HttpRequestV3.node.js:207:39) at WorkflowExecute.runNode (/usr/local/lib/node_modules/n8n/node_modules/n8n-core/dist/execution-engine/workflow-execute.js:632:42) at /usr/local/lib/node_modules/n8n/node_modules/n8n-core/dist/execution-engine/workflow-execute.js:881:62 at processTicksAndRejections (node:internal/process/task_queues:95:5) at /usr/local/lib/node_modules/n8n/node_modules/n8n-core/dist/execution-engine/workflow-execute.js:1215:20




- ERRO
JSON.parse: bad control character in string literal at line 3 column 37 of the JSON data




O erro "JSON.parse: bad control character in string literal" geralmente ocorre quando há caracteres de controle inválidos ou problemas de formatação no JSON. Vamos revisar o JSON e garantir que ele esteja corretamente formatado.

### JSON Corrigido

Certifique-se de que o JSON esteja corretamente formatado e que todas as aspas estejam fechadas corretamente. Aqui está o JSON corrigido:

```json
{
  "model": "mistral",
  "prompt": "Traduza para o {{$node['Codigo-Extrair-dados-do-post'].json['targetLanguage']}}: {{$node['Codigo-Extrair-dados-do-post'].json['content']}}. Importante manter a estrutura do post sem afetar a formatação ou elementos do wordpress.",
  "stream": false
}
```






Sim, é possível que o conteúdo do trecho `content` contenha caracteres que precisam ser escapados para que o JSON seja válido. Vamos garantir que todos os caracteres especiais no conteúdo sejam escapados corretamente.

### Função para Escapar Caracteres Especiais

Você pode usar uma função JavaScript para escapar caracteres especiais no conteúdo antes de incluí-lo no JSON. Aqui está um exemplo de como fazer isso:

```js
function escapeJsonString(str) {
  return str.replace(/\\/g, '\\\\')
            .replace(/"/g, '\\"')
            .replace(/\n/g, '\\n')
            .replace(/\r/g, '\\r')
            .replace(/\t/g, '\\t');
}

// O n8n passa os dados recebidos em um array chamado `items`
return items.map(item => {
  // Extrair o título do post
  const title = item.json.title?.rendered || 'Sem título';

  // Extrair o corpo do post (conteúdo) e escapar caracteres especiais
  const content = escapeJsonString(item.json.content?.rendered || 'Sem conteúdo');

  // Extrair metadados (exemplo: HREFLANG, idioma, etc.)
  const metadata = item.json.meta || {};

  // Extrair a URL da imagem de capa (featured image)
  const featuredImageUrl = item.json.featured_media_url || item.json._links?.['wp:featuredmedia']?.[0]?.href || 'Sem imagem de capa';

  const targetLanguage = 'inglês'; // Define o idioma de destino

  // Retornar os dados extraídos
  return {
    json: {
      title,
      content,
      metadata,
      featuredImageUrl,
      targetLanguage // Idioma de destino
      // Você pode adicionar outros campos aqui, se necessário
    }
  };
});
```

### Atualização do Corpo da Requisição JSON

Com o conteúdo escapado, você pode atualizar o corpo da requisição JSON no nó HTTP Request:

```json
{
  "model": "mistral",
  "prompt": "Traduza para o {{$node['Codigo-Extrair-dados-do-post'].json['targetLanguage']}}: {{$node['Codigo-Extrair-dados-do-post'].json['content']}}. Importante manter a estrutura do post sem afetar a formatação ou elementos do wordpress.",
  "stream": false
}
```




The service refused the connection - perhaps it is offline

Error details
From HTTP Request

Error code

ECONNREFUSED

Full message

connect ECONNREFUSED ::1:11434

Request

{ "body": { "model": "mistral", "prompt": "Traduza para o {{$node['Codigo-Extrair-dados-do-post'].json['targetLanguage']}}: {{$node['Codigo-Extrair-dados-do-post'].json['content']}}. Importante manter a estrutura do post sem afetar a formatação ou elementos do wordpress.", "stream": false }, "headers": { "content-type": "application/json", "accept": "application/json,text/html,application/xhtml+xml,application/xml,text/*;q=0.9, image/*;q=0.8, */*;q=0.7" }, "method": "POST", "uri": "http://localhost:11434/api/generate", "gzip": true, "rejectUnauthorized": true, "followRedirect": true, "resolveWithFullResponse": true, "followAllRedirects": true, "timeout": 300000, "encoding": null, "json": false, "useStream": true }

Other info


postgres-1         | 2025-02-05 14:47:15.315 UTC [27] LOG:  checkpoint starting: time
postgres-1         | 2025-02-05 14:47:16.827 UTC [27] LOG:  checkpoint complete: wrote 16 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.504 s, sync=0.004 s, total=1.512 s; sync files=15, longest=0.002 s, average=0.001 s; distance=37 kB, estimate=51 kB; lsn=0/1C88AB8, redo lsn=0/1C88A80
n8n                | connect ECONNREFUSED ::1:11434
n8n                | connect ECONNREFUSED ::1:11434





no step que faz HTTP request ao Ollama Local ocorre o erro abaixo:

Error code

ECONNREFUSED

Full message

connect ECONNREFUSED ::1:11434

o que pode ser?





- Verificando o workflow demo
- O host é diferente


- Ajustando
DE:
http://localhost:11434/api/generate
PARA:
http://ollama:11434/api/generate


então erro de conexão cessou!
então erro de conexão cessou!
então erro de conexão cessou!
então erro de conexão cessou!





[
  {
    "model": "mistral",
    "created_at": "2025-02-05T21:00:20.110432037Z",
    "response": " traduzir para o {{ $node['Codigo-Extrair-dados-do-post'].json['targetLanguage'] }}: {{ $node['Codigo-Extrair-dados-do-post'].json['content'] }} é importante manter a estrutura do post sem afetar a formatação ou elementos do WordPress.\n\nNão parece que essa string seja PHP, então não consegui identificar onde você deveria fazer essas modificações. Por favor forneça mais informações sobre como você está usando essa string para que possamos ajudá-lo corretamente.",
    "done": true,
    "done_reason": "stop",
    "context": [
      3,
      29473,
      [.........]
      29491
    ],
    "total_duration": 3181830400,
    "load_duration": 4767904,
    "prompt_eval_count": 87,
    "prompt_eval_duration": 3000000,
    "eval_count": 150,
    "eval_duration": 3172000000
  }
]



"response": " traduzir para o {{ $node['Codigo-Extrair-dados-do-post'].json['targetLanguage'] }}: {{ $node['Codigo-Extrair-dados-do-post'].json['content'] }} é importante manter a estrutura do post sem afetar a formatação ou elementos do WordPress.\n\nNão parece que essa string seja PHP, então não consegui identificar onde você deveria fazer essas modificações. Por favor forneça mais informações sobre como você está usando essa string para que possamos ajudá-lo corretamente.",




Ao utilizar o JSON:

~~~~json
{
  "model": "mistral",
  "prompt": "Traduza para o {{$node['Codigo-Extrair-dados-do-post'].json['targetLanguage']}}: {{$node['Codigo-Extrair-dados-do-post'].json['content']}}. Importante manter a estrutura do post sem afetar a formatação ou elementos do wordpress.",
  "stream": false
}
~~~~


traz a resposta:

~~~~

"response": " traduzir para o {{ $node['Codigo-Extrair-dados-do-post'].json['targetLanguage'] }}: {{ $node['Codigo-Extrair-dados-do-post'].json['content'] }} é importante manter a estrutura do post sem afetar a formatação ou elementos do WordPress.\n\nNão parece que essa string seja PHP, então não consegui identificar onde você deveria fazer essas modificações. Por favor forneça mais informações sobre como você está usando essa string para que possamos ajudá-lo corretamente.",

~~~~






no N8N, como eu faço para acessar valores do step anterior?

no step anterior o código é este:

~~~~js
function escapeJsonString(str) {
  return str.replace(/\\/g, '\\\\')
            .replace(/"/g, '\\"')
            .replace(/\n/g, '\\n')
            .replace(/\r/g, '\\r')
            .replace(/\t/g, '\\t');
}

// O n8n passa os dados recebidos em um array chamado `items`
return items.map(item => {
  // Extrair o título do post
  const title = item.json.title?.rendered || 'Sem título';

  // Extrair o corpo do post (conteúdo) e escapar caracteres especiais
  const content = escapeJsonString(item.json.content?.rendered || 'Sem conteúdo');

  // Extrair metadados (exemplo: HREFLANG, idioma, etc.)
  const metadata = item.json.meta || {};

  // Extrair a URL da imagem de capa (featured image)
  const featuredImageUrl = item.json.featured_media_url || item.json._links?.['wp:featuredmedia']?.[0]?.href || 'Sem imagem de capa';

  const targetLanguage = 'inglês'; // Define o idioma de destino

  // Retornar os dados extraídos
  return {
    json: {
      title,
      content,
      metadata,
      featuredImageUrl,
      targetLanguage // Idioma de destino
      // Você pode adicionar outros campos aqui, se necessário
    }
  };
});
~~~~

quero acessar o title, content e targetLanguage, para usar num prompt no JSON do próximo step que é um HTTP Request para um Ollama Local.

Como eu acesso estes valores?





No n8n, para acessar os valores do step anterior você utiliza as **expressões**. Por exemplo, se no step anterior você retornou os campos `title`, `content` e `targetLanguage`, você pode acessá-los no próximo step (como no HTTP Request) utilizando a sintaxe:

- **Título:** `{{$json.title}}`
- **Conteúdo:** `{{$json.content}}`
- **Idioma de destino:** `{{$json.targetLanguage}}`

### Exemplo no HTTP Request

Suponha que você queira enviar um JSON com esses valores para o endpoint do Ollama. No campo **Body Parameters** (em modo JSON) do nó HTTP Request, você pode usar:

```json
{
  "input": "={{ $json.content }}",
  "prompt": "Traduzir o post com título: {{$json.title}} para {{$json.targetLanguage}}.",
  "target_language": "={{ $json.targetLanguage }}"
}
```

Essa configuração irá pegar os valores retornados do step anterior e utilizá-los para compor a requisição que será enviada ao Ollama Local. Basta clicar no botão de “expressões” (ícone de ⚙️) e inserir a expressão conforme mostrado.






No n8n, para acessar os valores de um step anterior, você pode usar a sintaxe `$node[NomeDoStep].json[CampoQueVocêQuerAcessar]`. No seu caso, você quer acessar os campos `title`, `content` e `targetLanguage` do step anterior para usar em um prompt no próximo step, que é um HTTP Request para um Ollama Local.

Aqui está um exemplo de como você pode fazer isso:

### Passo 1: Certifique-se de que o step anterior está configurado corretamente
O código que você forneceu já está retornando os campos `title`, `content` e `targetLanguage` no formato JSON. Isso significa que esses campos estão disponíveis para serem acessados no próximo step.

### Passo 2: Configurar o HTTP Request para Ollama Local
No step do HTTP Request, você pode acessar os valores do step anterior da seguinte maneira:

1. **URL**: Defina a URL do seu Ollama Local.
2. **Método**: Geralmente, você usará `POST` para enviar dados.
3. **Headers**: Se necessário, adicione os headers apropriados (por exemplo, `Content-Type: application/json`).
4. **Body**: Aqui você vai construir o JSON que será enviado no corpo da requisição. Você pode acessar os valores do step anterior usando a sintaxe mencionada.

Exemplo de como configurar o Body do HTTP Request:

```json
{
  "prompt": "Traduza o seguinte texto para {{$node["NomeDoStepAnterior"].json["targetLanguage"]}}: {{$node["NomeDoStepAnterior"].json["title"]}}\n{{$node["NomeDoStepAnterior"].json["content"]}}"
}
```

### Explicação:
- `{{$node["NomeDoStepAnterior"].json["targetLanguage"]}}`: Acessa o valor de `targetLanguage` do step anterior.
- `{{$node["NomeDoStepAnterior"].json["title"]}}`: Acessa o valor de `title` do step anterior.
- `{{$node["NomeDoStepAnterior"].json["content"]}}`: Acessa o valor de `content` do step anterior.

### Passo 3: Executar o fluxo
Depois de configurar o HTTP Request com os valores do step anterior, você pode executar o fluxo e o n8n irá substituir as expressões `{{...}}` pelos valores correspondentes.

### Exemplo Completo:
Aqui está um exemplo completo de como o Body do HTTP Request pode ficar:

```json
{
  "prompt": "Traduza o seguinte texto para {{$node["NomeDoStepAnterior"].json["targetLanguage"]}}: {{$node["NomeDoStepAnterior"].json["title"]}}\n{{$node["NomeDoStepAnterior"].json["content"]}}"
}
```

Substitua `"NomeDoStepAnterior"` pelo nome real do step anterior no seu fluxo.

### Dica:
Se você estiver usando a interface gráfica do n8n, você pode clicar no ícone de "Expressão" (um ícone de chave inglesa) ao lado do campo onde deseja inserir o valor, e o n8n irá sugerir automaticamente os campos disponíveis dos steps anteriores.

Isso deve permitir que você acesse e utilize os valores `title`, `content` e `targetLanguage` no seu próximo step.






- Ajustar o JSON:

~~~~json
{
  "model": "mistral",
  "prompt": "Traduza o seguinte texto para {{$node["Codigo-Extrair-dados-do-post"].json["targetLanguage"]}}: {{$node["Codigo-Extrair-dados-do-post"].json["title"]}}\n{{$node["Codigo-Extrair-dados-do-post"].json["content"]}}",
  "stream": false
}
~~~~

funcionou
porém ele nao traduz direto, fica explicando as coisas



- Ajustar o JSON:

~~~~json
{
  "model": "mistral",
  "prompt": "Traduza o seguinte texto para {{$node["Codigo-Extrair-dados-do-post"].json["targetLanguage"]}}: {{$node["Codigo-Extrair-dados-do-post"].json["title"]}}\n{{$node["Codigo-Extrair-dados-do-post"].json["content"]}} . Preciso que o texto seja traduzido, não preciso de explicações a respeito do que ele é ou faz. Somente traduza o que foi fornecido.",
  "stream": false
}
~~~~


trouxe uma tradução, mas bem menor que o post original:



~~~~json
[
  {
    "model": "mistral",
    "created_at": "2025-02-06T15:11:26.86991565Z",
    "response": "1. Introdução\n     - DevOps e SRE (Site Reliability Engineering) são abordagens de engenharia em TI que visam aumentar a eficiência e confiabilidade dos sistemas.\n     - A adoção dessas abordagens pode trazer benefícios como melhoria na confiabilidade, eficiência e escalabilidade de sistemas TI.\n\n  2. DevOps\n     - O DevOps é uma prática que envolve a colaboração entre desenvolvedores e operações para criar um ciclo contínuo de desenvolvimento e implantação.\n     - Os principais objetivos do DevOps são aumentar a velocidade da entrega, reduzir o tempo de resposta e melhorar a qualidade dos sistemas TI.\n\n  3. SRE (Site Reliability Engineering)\n     - O SRE é uma abordagem que se baseia no conceito de \"todos os engenheiros são engenheiros de site confiável\" e foca em garantir a disponibilidade, a performance e a escalabilidade dos sistemas TI.\n     - O SRE envolve práticas como monitoramento contínuo, diagnóstico e correção rápida de problemas e melhoria contínua do sistema.\n\n  4. Docker\n     - O Docker é uma ferramenta de containerização que permite criar e gerenciar sistemas TI em containerizados, facilitando a movimentação dos mesmos entre ambientes diferentes.\n     - O uso do Docker pode trazer benefícios como melhoria na portabilidade, redução de tempo de implantação e escalabilidade horizontal.\n\n  5. Conclusão\n     - O Docker é uma peça-chave no quebra-cabeça DevOps e SRE. A adoção dessa tecnologia pode melhorar a confiabilidade, eficiência e escalabilidade de sistemas TI.",
    "done": true,
    "done_reason": "stop",
    "context": [
      3,
      29473,
      29491
    ],
    "total_duration": 11499820761,
    "load_duration": 4840658,
    "prompt_eval_count": 2048,
    "prompt_eval_duration": 1003000000,
    "eval_count": 487,
    "eval_duration": 10490000000
  }
]
~~~~




- Testar DeepSeek via Ollama

https://www.datacamp.com/tutorial/deepseek-r1-ollama

Step 2: Download and run DeepSeek-R1

Let’s test the setup and download our model. Launch the terminal and type the following command.

ollama run deepseek-r1

Step 2: Accessing DeepSeek-R1 via API

To integrate DeepSeek-R1 into applications, use the Ollama API using curl:

curl http://localhost:11434/api/chat -d '{
  "model": "deepseek-r1",
  "messages": [{ "role": "user", "content": "Solve: 25 * 25" }],
  "stream": false
}'

https://ollama.com/library/deepseek-r1

ollama run deepseek-r1:671b

# ollama run deepseek-r1:671b
pulling manifest 
pulling 9801e7fce27d...   0% ▕                                                                                                                                                                                                                                                           ▏  36 MB/404 GB  7.9 MB/s  14h15m^C

ollama run deepseek-r1

# ollama run deepseek-r1
pulling manifest 
pulling 96c415656d37...   1% ▕█                                                                                                                                                                                                                                                          ▏  29 MB/4.7 GB  7.3 MB/s  10m36s


- Baixando o deepseek-r1 de 4,7GB, pois o deepseek-r1:671b pesa 404GB:


# ollama run deepseek-r1
pulling manifest 
pulling 96c415656d37...  13% ▕███████████████████████████████                                                                                                                                                                                                                            ▏ 591 MB/4.7 GB   10 MB/s   6m15s





- ANTES

> df -h
Filesystem      Size  Used Avail Use% Mounted on
none            7.8G     0  7.8G   0% /usr/lib/modules/5.15.167.4-microsoft-standard-WSL2
none            7.8G  4.0K  7.8G   1% /mnt/wsl
drivers         150G  144G  5.4G  97% /usr/lib/wsl/drivers
/dev/sdc       1007G   33G  924G   4% /


- DEPOIS

> ncdu
> ncdu -x /
> df -h
Filesystem      Size  Used Avail Use% Mounted on
none            7.8G     0  7.8G   0% /usr/lib/modules/5.15.167.4-microsoft-standard-WSL2
none            7.8G  4.0K  7.8G   1% /mnt/wsl
drivers         150G  145G  5.4G  97% /usr/lib/wsl/drivers
/dev/sdc       1007G   30G  926G   4% /




# ollama run deepseek-r1
pulling manifest 
pulling 96c415656d37... 100% ▕███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏ 4.7 GB                         
pulling 369ca498f347... 100% ▕███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏  387 B                         
pulling 6e4c38e1172f... 100% ▕███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏ 1.1 KB                         
pulling f4d24e9138dd... 100% ▕███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏  148 B                         
pulling 40fb844194b2... 100% ▕███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏  487 B                         
verifying sha256 digest 
writing manifest 
success 
>>> Send a message (/? for help)



- Tratar espaço em disco do Windows vs WSL.
1. ncdu
2. EXCLUIR mistral
3. TRATAR DISCO DO WSL, analisar pastas locais mapeadas e Container do Ollama.





# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## PENDENTE

- Comandos para subir ambiente:

~~~~bash
git clone https://github.com/n8n-io/self-hosted-ai-starter-kit.git
cd self-hosted-ai-starter-kit

cd /home/fernando/cursos/n8n/self-hosted-ai-starter-kit
docker compose --profile gpu-nvidia up

accessible via:
n8n                | http://localhost:5678/
~~~~

- Tratar disco c: do Windows

- Efetuar testes com n8n
    1. seguir README:
    <https://github.com/n8n-io/self-hosted-ai-starter-kit/blob/main/README.md>
    2. seguir fluxo resumido/sugerido pelo DeepSeek
    3. Ver sobre "Function Node" no n8n, para executar códigos JavaScript para obter o JSON e processar os dados recebidos.


- Tratar espaço em disco do Windows vs WSL.
1. ncdu
2. EXCLUIR mistral
3. TRATAR DISCO DO WSL, analisar pastas locais mapeadas e Container do Ollama.

- Avaliar uso do DeepSeek no lugar do Ollama.
