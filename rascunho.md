


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
##  PENDENTE

- Subir VM com Ubuntu 24 + Python3:
instalar python mais recente
configurar venv??
instalar as dependencias do projeto via pip3
efetuar teste do script

- Tentar instalar dependencias no Python3 do Debian-10.
configurar venv??