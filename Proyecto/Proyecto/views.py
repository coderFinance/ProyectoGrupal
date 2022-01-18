from django.http import HttpResponse

def inicio(req):
    return HttpResponse("Funciona")