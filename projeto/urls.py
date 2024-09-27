"""
URL configuration for Projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.http import HttpResponse

def sobre_view(request):
    return HttpResponse("Nascida do amor pela natureza e pela arte de criar, a Floricultura do Vale é um sonho realizado em um pequeno vilarejo mineiro. Com a missão de levar beleza e emoção através das flores, transformamos cada pedido em uma obra de arte única.")

def user_view(request, username):
    if username=='Roberto':
        return HttpResponse(f"Bem vindo Chefe {username}!")
    else: 
        return HttpResponse(f"Bem vindo {username}!")
    
def root_view(request):
    return HttpResponse("Página inicial do site/Root <p> sobre/ <p> user/nome_do_usuario <p> contato/")

def contato_view(request):
    return HttpResponse("Para encomendas e orçamentos, mande um e-mail para floridovale@gmail.com ou mande uma mensagem para o número (35) 9 9087-7659")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre/', sobre_view),
    path('user/<str:username>', user_view),
    path('', root_view),
    path('contato', contato_view)
]
