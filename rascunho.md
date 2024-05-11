


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

