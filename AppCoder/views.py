from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso


# Create your views here.
def inicio(request):
    return HttpResponse("vista inicio")

def cursos(request):
    return HttpResponse("vista cursos")

def profesores(request):
    return HttpResponse("vista profesores")

def entregables(request):
    return HttpResponse("vista entregables")

def estudiantes(request):
    return HttpResponse("vista estudiantes")