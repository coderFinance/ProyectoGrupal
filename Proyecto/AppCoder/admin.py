from django.contrib import admin

from AppCoder.models import Alumno, Curso, Docentes

# Register your models here.

admin.site.register(Alumno)
admin.site.register(Docentes)
admin.site.register(Curso)
