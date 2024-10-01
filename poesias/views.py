from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def sobre_view(request):
    return render(request, 'sobre.html')

def user_view(request, username):
    if username=='Roberto':
        return HttpResponse(f"Bem vindo Chefe {username}!")
    else: 
        return HttpResponse(f"Bem vindo {username}!")
    
def root_view(request):
    return HttpResponse("Página ROOT.")

def contato_view(request):
    return render(request, 'contatos.html') 

def produto_view(request):
    return render(request, 'produtos.html')

def contexto(request):
    context = {
        'nome': 'João',
        'idade': 30,
        'hobbies': ['Leitura', 'Ciclismo', 'Cozinhar']
}
    return render(request, 'contexto.html', context)

