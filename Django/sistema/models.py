from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)



#classes
#modelo -> tabela no bd
# Cada atributo -> coluna na tabela