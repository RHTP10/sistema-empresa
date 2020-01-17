from django.db import models

# Create your models here.

class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
