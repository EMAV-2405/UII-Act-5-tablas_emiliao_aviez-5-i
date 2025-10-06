from django.contrib import admin
from .models import Cliente # Asegúrate de que el nombre del modelo coincida (Cliente en vez de clientes si es la clase que definimos)

# Register your models here.

# Corrección aquí: 'site' en lugar de 'sitie'
admin.site.register(Cliente)