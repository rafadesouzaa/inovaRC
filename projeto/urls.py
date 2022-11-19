"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import home, sobre, formPessoa, create, consultaPessoa, login, dash, grafico
from app import views #adicionado Carol 29-05

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login),
    path('login/', login),
    path('home/', home, name="home"),
    path('sobre/', sobre, name="sobre"),
    path('dash/', dash, name="dash"),
    path('grafico/', grafico, name="grafico"),

    path('cadastrar-pessoa/', formPessoa, name="cadastrar-pessoa"),
    path('create/', create, name="create"),
    path('consulta-pessoa',consultaPessoa,name="consulta-pessoa"),
    
    
    
]
