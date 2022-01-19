from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import Curso

# Create your views here.

def crea_curso(self):
    
    curso = Curso(grado = "5", division = "A")

    curso.save()

    return HttpResponse(f'Se creo el curso {curso.grado}{curso.division}')