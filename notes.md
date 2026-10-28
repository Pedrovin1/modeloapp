# Dir

## os.path.*dirname*()
L-> retorna o path até o diretório aonde o arquivo/path inserido se encontra

Ex: 
os.path.dirname(pasta1/subpasta/arquivo)
retorna --> pasta1/subpasta

---

# Decouple

## config('keyTextHere', default='', cast=type)
L-> busca no .env por uma key retorna o valor, usando o default caso não encontre no .env e convertendo para o type especificado.

# Installed App

# STATIC_URL
L-> declara o nome que a pasta de static files do frontend no navegador terá

---

# apps

## name='appFolderName'

"must match the name of the app's directory and is used by Django to locate and load the app." \[ [link](https://django-tutorial.dev/course/django-for-beginners/app-structure/appspy/) \]

## verbose_name = 'nomeAqui'
 L-> apenas para traduções

# class Meta
L-> Trata os dados resgatados do banco, para fins diversos, como fornecer ao Template em uma ordem específica por exemplo

# Models

## Oracle Databse Table Names

Novas tabelas criadas através do makemigrations + migrate seguem a convenção:

\[ NOME_DO_APP + NOME_DO_MODEL \]