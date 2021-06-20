"""ayudaPeludo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
import appPeludo.views

urlpatterns = [
    #Rutas para levantar cada página
    path('admin/', admin.site.urls),
    path('', appPeludo.views.home, name= 'home'),
    path('consultaClima/', appPeludo.views.consultaClima, name= 'consultaClima'),
    path('index/', appPeludo.views.index, name= 'index'),
    path('formulario/', appPeludo.views.formulario, name= 'formulario'),
    path('test/', appPeludo.views.test, name= 'test'),
    path('menuPerros/', appPeludo.views.menuPerros, name= 'menuPerros'),
    path('menuGatos/', appPeludo.views.menuGatos, name= 'menuGatos'),
    path('consultaClima/', appPeludo.views.consultaClima, name= 'consultaClima'),

    #Rutas de cada función
    path('crearMascota/', appPeludo.views.crearMascota, name= 'crearMascota'),
    path('listarMascotas/', appPeludo.views.listarMascotas, name= 'listarMascotas'),
    path('crearMascotaNav/<str:codigo>/<str:nombre>/', appPeludo.views.crearMascotaNav, name= 'crearMascotaNav'),
    path('leerMascota/<int:id>', appPeludo.views.leerMascota, name='leerMascota'),
    path('editarMascota/<int:id>', appPeludo.views.editarMascota, name='editarMascota'),
    path('borrarMascota/<int:id>', appPeludo.views.borrarMascota, name='borrarMascota'),

    #Guardar datos con formulario
    path('nuevaMascota/', appPeludo.views.nuevaMascota, name='nuevaMascota'),
    path('agregarMascota/', appPeludo.views.agregarMascota, name='agregarMascota'),

    #Rutas para formularios
    path('formMascotas/', appPeludo.views.formMascotas, name='formMascotas'),
    path('formMascotasEdit/<int:id>/', appPeludo.views.formMascotasEdit, name='formMascotasEdit'),

    #Rutas API
    path("api/", include("restMascota.urls")),
]
