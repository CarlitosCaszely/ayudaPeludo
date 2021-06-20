from django.contrib import admin
from .models import Mascotas, Categoria, Cliente
# Register your models here.
admin.site.register(Mascotas)
admin.site.register(Categoria)
admin.site.register(Cliente)