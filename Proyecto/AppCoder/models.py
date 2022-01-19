from email import charset
from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField("nombre", max_length=50)
    apellido = models.CharField("apellido", max_length=50)
    año_nacimiento = models.DateField("fecha", auto_now=False, auto_now_add=False)

class Docentes(models.Model):
    nombre = models.CharField("nombre", max_length=50)
    apellido = models.CharField("apellido", max_length=50)
    telefono = models.IntegerField()

class Curso(models.Model):
    grado = models.IntegerField()
    division = models.CharField("division", max_length=1)
