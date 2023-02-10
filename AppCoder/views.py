from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso


# Create your views here.
def inicio(request):
    return render (request, 'AppCoder/inicio.html')

    #return HttpResponse("vista inicio")

def cursos(request):
    return render (request, 'AppCoder/cursos.html')

    #return HttpResponse("vista cursos")

def profesores(request):
        return render (request, 'AppCoder/profesores.html')

   # return HttpResponse("vista profesores")

def entregables(request):
    return render (request, 'AppCoder/entregables.html')

    #return HttpResponse("vista entregables")

def estudiantes(request):
    return render (request, 'AppCoder/estudiantes.html')

    #return HttpResponse("vista estudiantes")