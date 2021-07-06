from django.urls import path
from restMascota.views import listarMascotasRest, detalleMascotas
from restMascota.viewsLogin import login
urlpatterns = [
    path("listarMascotasRest/", listarMascotasRest, name="listarMascotasRest"),
    path("detalleMascotas/<str:codigo>/",detalleMascotas, name ="detalleMascotas"),
    path("login/",login, name="login"),
]
