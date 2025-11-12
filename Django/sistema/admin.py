from django.contrib import admin
from sistema import models

# Register your models here, e


#Passa quais as infos que devem ser exibidas
@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf', 'telefone', 'endereco')