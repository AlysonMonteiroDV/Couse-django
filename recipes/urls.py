from django.urls import path
from django.http import HttpResponse
from recipes.views import home
#   Cliente         Servidor
#HTTP REQUEST <- HTTP RESPONSE

urlpatterns = [
    path('', home),
    
    
    

]
