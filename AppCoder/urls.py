from django.urls import path
from AppCoder.forms import *
from AppCoder.views import *
from django import forms

urlpatterns = [
    path("inicio/", inicio, name="Inicio"),
    path("vercursos/", ver_curso, name="VerCurso"),
    path("verestudiantes/", ver_estudiante, name="VerEstudiante"),
    path("verprofesores/", ver_profesor, name="VerProfesor"),
    path("cursos_form/", cursoform, name="CursoForm"),
    path("profesores_form/", profesoresform, name="ProfesoresForm"),
    path("estudiantes_form/", estudiantesform, name="EstudiantesForm"),
]