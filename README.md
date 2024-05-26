# wordpress-blog-post-with-python

WordPress is one of the most popular and widely-used tools to create blogs, e-commerce platforms, and websites.

I'll show you how to create content automatically and push it to your WordPress website with Python.

This is how it works:

    We'll get content from our source (for example, another website we run)
    We'll translate it into our language
    We'll choose a featured image already available on our website and finally publish it to our WordPress instance as a post.




## DETALHES
- Utilizada a biblioteca deep-translator
Devido erro AttributeError: 'NoneType' object has no attribute 'group' geralmente ocorre quando a biblioteca googletrans não consegue obter o token de autenticação necessário para a tradução. Isso pode ser devido a mudanças na API do Google Translate, problemas temporários com o serviço ou a versão da biblioteca.

Para resolver isso, podemos tentar uma das seguintes abordagens:

    Atualizar a biblioteca googletrans: Verifique se está usando a versão mais recente da biblioteca googletrans.

    Usar uma biblioteca alternativa: Se a atualização não resolver o problema, considere usar uma biblioteca alternativa como deep-translator, que também oferece suporte para tradução com o Google Translate.

Aqui está um exemplo de como usar a biblioteca deep-translator: