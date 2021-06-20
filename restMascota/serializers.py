from rest_framework import fields, serializers
from appPeludo.models import Mascotas

class MascotasSerializer(serializers.ModelSerializer):
    class Meta:
        model= Mascotas
        fields=["codigo","nombre","especie","adoptado"]