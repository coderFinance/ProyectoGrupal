from django.urls import path
from AppCoder import views
from AppCoder.models import Curso
from AppCoder.views import crea_curso, cursos, docentes, alumnos#, inicio
from Proyecto.views import inicio #, inicioConTemplate


urlpatterns = [
    path("", inicio, name="inicio"),
    #path("probandoTemplate", inicioConTemplate),
    path("creaCurso", crea_curso),
    path("alumnos", alumnos, name="alumnos"),
    path("cursos", cursos, name="cursos"),
    path("docentes", docentes, name="docentes")
]