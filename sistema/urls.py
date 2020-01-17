
from django.contrib import admin
from django.urls import path
from usuario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mostrar_formulario_cadastro),
    path('login', views.login),
    path('pessoas', views.mostrar_pessoas),
]
