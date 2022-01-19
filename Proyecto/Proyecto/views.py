from json import load
from django.template.context import Context
from django.template import Template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def inicio(req):
    return render(req, "Inicio.html")

# def inicioConTemplate(req):

#     dic = {
#         "nombre": "Juan",
#         "apellido": "Perez"
#     }

#     plantilla = loader.get_template("Inicio.html")

#     documento = plantilla.render(dic)

#     return HttpResponse(documento)

    