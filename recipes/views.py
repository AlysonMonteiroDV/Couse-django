from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse


def home(request):
    return HttpResponse("HOME PAGE")

def contato(request):
    return HttpResponse("CONTATO")

def my_view(request):
    return HttpResponse("One Beautiful String")

def sobre(request):
    return HttpResponse("About")

def temas(request):
    return HttpResponse("teme page with django in recipes")
# Create your views here.
