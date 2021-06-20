from django.db import models

# Create your models here.
class Mascotas(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=10)
    adoptado = models.BooleanField(max_length=10)

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)

class Cliente(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    correo = models.TextField(max_length=100)
    direccion = models.TextField(max_length=100)

