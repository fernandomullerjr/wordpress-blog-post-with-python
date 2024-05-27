





# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
# #################################################################################################################################################
## COMANDOS

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

- Ver como pegar no JSON a capa do Post, imagem destaque, etc. Verificar demais melhoriais que é possível realizar.
- Testar com o Blog devopsmind.
- Fixar versões contidas no "requirements.txt", definir versões exatas.
- Criar Dockerfile e docker-compose, posteriormente. Avaliar melhores práticas.
- Ver forma de acionar fácil o script para um blog e post especifico, chamar uma CLI que vai perguntando os dados desejados. Usar Makefile +CLI??? Variar ambiente virtual??? Avaliar as opções.
- Ver como obter os JSON de blogs do exterior e automatizar o processo de criar um post, com base na página do exterior, adicionar menções ao DevOps Mind no cabeçalho.
- Adicionar try, exception, logs de erros.
- Testar combo "Fedora 40 + PyTorch" , <https://www.tudocelular.com/tech/noticias/n219464/fedora-linux-40-beta-lancado-gnome-46-ia.html>
