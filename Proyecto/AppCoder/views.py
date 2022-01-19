from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import Curso, Alumno, Docentes

# Create your views here.

def alumnos(req):
    return render(req, "Alumnos.html")

def docentes(req):
    return render(req, "Docentes.html")

def cursos(req):

    listaDeCursos = Curso.objects.all()

    return render(req, "Cursos.html", {"listaDeCursos": listaDeCursos})

def crea_curso(req):

    if (req.method == "POST"):
        curso = Curso(req.POST["grado"], req.POST["division"])

        curso.save()

        return render(req, "inicio.html")

    return render(req, "CursoNuevo.html")


# def crea_curso(self):
    
#     curso = Curso(grado = "5", division = "A")

#     curso.save()

#     return HttpResponse(f'Se creo el curso {curso.grado}{curso.division}')