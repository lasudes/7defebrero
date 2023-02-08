from django.db import models

# Create your models here.

class Estudiante(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.PositiveIntegerField(blank=True)

class Profesor(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    profesion = models.CharField(max_length=20)

class Curso(models.Model):
    
    tipo = models.CharField(max_length=40)
    comision = models.PositiveIntegerField(blank=True)
    duracion = models.PositiveIntegerField(blank=True)

    