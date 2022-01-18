from django.http import HttpResponse
from django.shortcuts import render

def inicio(req):
    return HttpResponse("Funciona")