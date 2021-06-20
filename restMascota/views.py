from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response, responses
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.serializers import Serializer
from appPeludo.models import Mascotas
from .serializers import MascotasSerializer

@csrf_exempt
@api_view(["GET","POST"])
def listarMascotasRest(request):
    # Lista de todas las mascotas
    if request.method == "GET":
        mascotas = Mascotas.objects.all()
        serializer = MascotasSerializer(mascotas, many =True)
        return Response(serializer.data)
    elif request.method== "POST":
        data= JSONParser().parse(request)
        serializer = MascotasSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def detalleMascotas(request, codigo):
    try:
        mascota= Mascotas.objects.get(codigo=codigo)
    except Mascotas.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = MascotasSerializer(mascota)
        return Response(serializer.data)
    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = MascotasSerializer(mascota, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    if request.method =="DELETE":
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    