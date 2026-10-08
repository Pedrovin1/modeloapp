# Dir

## os.path.*dirname*()
L-> retorna o path até o diretório aonde o arquivo/path inserido se encontra

Ex: 
os.path.dirname(pasta1/subpasta/arquivo)
retorna --> pasta1/subpasta

---

# Decouple

## config('keyTextHere', default='', cast=type)
L-> busca no .env por uma key retorna, usando o default coso não encontre no .env e convertendo para o tipo especificado.

# Installed App

# STATIC_URL
L-> declara o nome que a pasta de static files do frontend no navegador terá

---

# apps

## name='appFolderName'

"must match the name of the app's directory and is used by Django to locate and load the app." [https://django-tutorial.dev/course/django-for-beginners/app-structure/appspy/]