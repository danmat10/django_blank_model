<html>
<head>
  <title>README</title>
</head>
<body>

<h1>Configuração do Projeto Django</h1>

<p>Este documento descreve os passos necessários para configurar e rodar um projeto Django.</p>

<h2>Pré-requisitos</h2>

<ul>
  <li>Python 3.8 ou superior</li>
  <li>Pip (gerenciador de pacotes Python)</li>
</ul>

<h2>Configuração do Ambiente Virtual (venv)</h2>

<ol>
  <li>Navegue até o diretório onde você quer criar seu projeto Django e crie um novo ambiente virtual:</li>
  
  <pre><code>python3 -m venv myvenv</code></pre>
  
  <li>Ative o ambiente virtual:</li>
  
  <pre><code>source myvenv/bin/activate</code></pre>
  
  <p><i>Nota: Em sistemas Windows, o comando de ativação é:</i></p>
  
  <pre><code>myvenv\Scripts\activate</code></pre>
</ol>

<h2>Instalação do Django</h2>

<p>Com o ambiente virtual ativado, instale o Django:</p>

<pre><code>pip install django</code></pre>

<h2>Criação do Projeto Django</h2>

<p>Crie um novo projeto Django:</p>

<pre><code>django-admin startproject myproject</code></pre>

<h2>Criação de uma Aplicação Django</h2>

<p>No diretório do projeto Django, crie uma nova aplicação:</p>

<pre><code>python manage.py startapp myapp</code></pre>

<h2>Configuração do Django</h2>

<p>No arquivo myproject/settings.py, adicione a nova aplicação à lista INSTALLED_APPS:</p>

<pre><code>
INSTALLED_APPS = [
    'myapp',
    ...
]
</code></pre>

<h3>Adicionar as configurações de pt-BR e o horário de São Paulo</h3>

<pre><code>
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True
</code></pre>

<h3>Adicionar o diretório dos templates</h3>

<pre><code>
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'myapp/templates')],
        ...
    },
]
</code></pre>

<h2>Criação de URLs</h2>

<ol>
  <li>Crie um arquivo urls.py no diretório da aplicação (se não existir) e defina as URLs:</li>

<pre><code>
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
</code></pre>

  <li>Inclua as URLs da aplicação no projeto principal. Em myproject/urls.py, adicione uma linha para as URLs da aplicação:</li>

<pre><code>
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('myapp/', include('myapp.urls')),
    path('admin/', admin.site.urls),
]
</code></pre>
</ol>

<h2>Criação de uma View</h2>

<p>No arquivo views.py da aplicação, crie a view home:</p>

<pre><code>
from django.http import HttpResponse

def home(request):
    return HttpResponse("

Olá, Mundo!")
</code></pre>

<h2>Migrações</h2>

<p>Após definir os modelos em models.py, crie as migrações e aplique-as ao banco de dados:</p>

<pre><code>
python manage.py makemigrations myapp
python manage.py migrate
</code></pre>

<h2>Criação de um Superusuário</h2>

<p>Crie um superusuário para o site:</p>

<pre><code>
python manage.py createsuperuser
</code></pre>

<h2>Rodando o servidor Django</h2>

<p>Rode o servidor:</p>

<pre><code>
python manage.py runserver
</code></pre>

<p>Isso iniciará o servidor Django no endereço http://127.0.0.1:8000/. Agora você tem um projeto Django básico rodando.</p>

<p>Para personalizar ainda mais seu projeto, você pode começar a adicionar modelos ao arquivo models.py da sua aplicação, criar views em views.py e adicionar templates em um diretório templates dentro da sua aplicação.</p>

<p>Por favor, visite a <a href="https://docs.djangoproject.com/">documentação oficial do Django</a> para mais detalhes e orientações adicionais.</p>

<h2>Contribuição</h2>

<p>Sinta-se à vontade para contribuir com este projeto. Qualquer feedback, correção ou adição são bem-vindos!</p>

</body>
</html>
