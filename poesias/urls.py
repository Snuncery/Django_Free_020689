"""
URL configuration for projeto project.

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
from django.urls import path, include
from poesias.views import contexto, sobre_view, user_view, root_view, contato_view, home, produto_view, guilherme_view, pextends, poema_detail, category, author

urlpatterns = [
    path('sobre/', sobre_view),
    path('user/<str:username>', user_view),
    path('', home),
    path('contato', contato_view),
    path('contexto', contexto),
    path('produtos', produto_view),
    path('guilherme', guilherme_view),
    path('page_extends/', pextends),
    path('poema_details/', poema_detail),
    path('poemas/categoria/<int:category_id>', category, name='category_id'),
    path('poemas/autor/<int:author_id>', author, name='author_id'),
]
