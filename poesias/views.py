from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from faker import Faker
from .models import Book

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

def guilherme_view(request):
    return render(request, 'guilherme.html')

def pextends(request):
    return render(request, 'page_extends.html')

fake = Faker('pt_BR')

def make_poetry():
    return{
        'title': fake.sentence(nb_words=5),
        'full_text': fake.text(250),
        'created_at': fake.date_time(),
        'author':{
            'first_name': fake.first_name,
            'last_name': fake.last_name,
        },
        'genre':{
            'name': fake.word
        },
        'cover':{
            'url': 'https://loremflickr.com/320/320/poetry,book',
        },
        'is_popular': fake.boolean()
    }

def poema_detail(request):
    poetry = make_poetry()
    return render(request, 'poema_detail.html', {'poetry': poetry})

def category(request, category_id):
    books = Book.objects.filter(
        categories__id=category_id,
    )

    if not books:
        raise Http404("Not found")
    
    return render(request, 'category.html', context={
        'books': books,
        'title': f'Categoria: {books.first().categories.all()[0]}'
    })

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books_detail.html', {'book': book})

def books_by_author(request, author_id):
    books = get_object_or_404(Book, author_id=author_id)
    return render(request, 'books_by_author.html', {'books': books})

def category_404(request, category_id):
    books = get_list_or_404 (Book.objects.filter(categories__id=category_id,))

    print("Books: ", books)
    print("Books: ", books[0])
    print("Books: ", books[0].categories.all()[0])

    return render(request, 'category404.html', context={
        'books': books,
        'title': f'Categoria: {books[0].categories.all()[0]}'
    })