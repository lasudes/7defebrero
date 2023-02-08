from django.urls import path
from AppCoder.views import *
urlpatterns = [
    path("vercursos/", ver_curso),
    path("verestudiantes/", ver_estudiante),
    path("verprofesores/", ver_profesor),
]