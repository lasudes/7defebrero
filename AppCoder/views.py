from django.shortcuts import render
from AppCoder.models import *
# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def ver_estudiante(request):

    estudiantes = Estudiante.objects.all

    return render(request, "AppCoder/verEstudiantes.html", {"estudiantes":estudiantes})

def ver_profesor(request):

    profesores = Profesor.objects.all

    return render(request, "AppCoder/verProfesores.html", {"profesores":profesores})

def ver_curso(request):

    cursos = Curso.objects.all

    return render(request, "AppCoder/verCursos.html", {"cursos":cursos})