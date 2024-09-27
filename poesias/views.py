from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def sobre_view(request):
    return HttpResponse("Nascida do amor pela natureza e pela arte de criar, a Floricultura do Vale é um sonho realizado em um pequeno vilarejo mineiro. Com a missão de levar beleza e emoção através das flores, transformamos cada pedido em uma obra de arte única.")

def user_view(request, username):
    if username=='Roberto':
        return HttpResponse(f"Bem vindo Chefe {username}!")
    else: 
        return HttpResponse(f"Bem vindo {username}!")
    
def root_view(request):
    return HttpResponse("Página ROOT.")

def contato_view(request):
    return HttpResponse("Para encomendas e orçamentos, mande um e-mail para floridovale@gmail.com ou mande uma mensagem para o número (35) 9 9087-7659")


# Create your views here.
