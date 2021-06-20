from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.utils import html
from appPeludo.models import Mascotas
from appPeludo.forms import mascotasForm
#Creación de una clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()

# Create your views here.
def home(request):
    return render(request,"index.html")

def consultaClima(request):
    return render(request, "consultaClima.html")

def formulario(request):
    return render(request, "formulario.html")

def index(request):
    return render(request,'index.html')

def menuPerros(request):
    return render(request,'PerfilesPerros/PerrosEnAdopcion.html')

def menuGatos(request):
    return render(request,'PerfilesGatos/GatosEnAdopcion.html')

def consultaClima(request):
    return render(request,'consultaClima.html')

def test(request):
    lista=["Godswar", "Paladins", "Valorant", "CSGO", "Apex"]

    nino=Persona("Fernando","8")

    contexto = {"nombre":"Claudia Andrea", "juegos":lista, "nino":nino}

    return render(request, "test.html", contexto)

def crearMascota(request):
    mascota = Mascotas(
        codigo = "MAS003",
        nombre = "Carlos",
        especie = "Pepo",
        adoptado = True
    )
    mascota.save()
    return HttpResponse ("Mascota Creada")

def crearMascotaNav(request, codigo, nombre):
    mascota = Mascotas(
        codigo = codigo,
        nombre = nombre,
        especie = "",
        adoptado = 0
    )
    mascota.save()
    return redirect(listarMascotas)

def listarMascotas(request):
    mascota = Mascotas.objects.all()
    return render(request, 'listaMascotas.html', {'Mascotas':mascota})

def leerMascota(request, id):
    mascota = Mascotas.objects.get(id=id)
    return HttpResponse(f"La mascota es: {mascota.codigo}, {mascota.nombre}")

def editarMascota(request,id):
    mascota = Mascotas.objects.get(id=id)
    mascota.nombre = "Pastita"
    mascota.save()
    return HttpResponse(f"El nuevo nombre de la mascota es: {mascota.nombre}")

def borrarMascota(request,id):
    mascota = Mascotas.objects.get(id=id)
    mascota.delete()
    return redirect(listarMascotas)
    
def nuevaMascota(request):
    return render(request,"nuevaMascota.html")

def agregarMascota(request):
    codigo = request.POST["codigo"]
    nombre = request.POST["nombre"]
    mascota = Mascotas(
        codigo = codigo,
        nombre = nombre,
        especie = "",
        adoptado = 0
    )
    mascota.save()
    return redirect(listarMascotas)

def formMascotas(request):
    datos={
        "form" : mascotasForm()
    }
    if request.method == "POST":
        formulario = mascotasForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos["mensaje"] = "Datos guardados correctamente"

    return render(request,"nuevaMascotaForm.html", datos)

def formMascotasEdit(request,id):
    mascota = Mascotas.objects.get(id=id)
    datos={
        "form" : mascotasForm(instance=mascota)
    }
    if request.method == "POST":
        formulario = mascotasForm(data=request.POST, instance=mascota)
        if formulario.is_valid:
            formulario.save()
            datos["mensaje"] = "Se ha modificado correctamente"
    return render(request,"editarMascotaForm.html", datos)
