
from django.contrib import admin
from django.urls import path
from usuario.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastrar_pessoa', mostrar_formulario_cadastro),
    path('login', login),
    path('pessoas', mostrar_pessoas),
    path('delete/<int:id>', delete),
    path('update/<int:id>', update),
    path('', home),
 
]
