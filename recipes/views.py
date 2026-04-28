from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html',{
        'name': 'Alyson',

    }) #namespace do home
    #render é uma função que recebe o request,
    #  o nome do template e um dicionário de
    #  contexto (opcional) e retorna um HttpResponse
    #  com o conteúdo do template renderizado.
    #  O dicionário de contexto é usado para passar
    #  dados do view para o template,
    #  permitindo que você exiba informações dinâmicas na página.

def contato(request):
    return HttpResponse("CONTATO")

def my_view(request):
    return HttpResponse("One Beautiful String")

def sobre(request):
    return render(request, 'recipes/contato.html')

def temas(request):
    return HttpResponse("teme page with django in recipes")
# Create your views here.
