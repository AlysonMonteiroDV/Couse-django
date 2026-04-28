from django.urls import path
from django.http import HttpResponse
from recipes.views import home, contato, sobre,temas
#   Cliente         Servidor
#HTTP REQUEST <- HTTP RESPONSE

urlpatterns = [
    path('', home),
    path('home/', home),
    path('contato/', contato),
    path('sobre/', sobre),
    path('recipes/temas', temas)

]
