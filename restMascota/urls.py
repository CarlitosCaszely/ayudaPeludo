from django.urls import path
from restMascota.views import listarMascotasRest, detalleMascotas
urlpatterns = [
    path("listarMascotasRest/", listarMascotasRest, name="listarMascotasRest"),
    path("detalleMascotas/<str:codigo>/",detalleMascotas, name ="detalleMascotas")
]
