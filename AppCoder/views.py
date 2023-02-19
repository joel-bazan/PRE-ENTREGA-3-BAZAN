from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import CursoFormulario


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
    
"""def curso(self):
        curso=Curso(nombre="Desarrollo Web"), camada=19881
        curso.save()
        documentoDeTexto=f"--->Curso:{curso.nombre} Camada: {curso.camada}
        return HttpResponse(documentoDeTexto)
        
def cursoFormulario(request):
     if request.method=="POST":
          curso=Curso(request.POST['curso'],(request.POST['camada']))
          curso.save()
          return render (request, "AppCoder/inicio.html")
     
     return render(request,"Appcoder/cursoFormulario.html")

"""
def cursoFormulario(request):
    if request.method=="POST":
        miFormulario=CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
               informacion=miFormulario.cleaned_data
               curso=Curso(nombre=informacion['curso'],comision=informacion['comision'])
               curso.save()
               return render(request, "AppCoder/inicio.html")

    else:
         miFormulario=CursoFormulario()
    
    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario":miFormulario})

#def busquedaCamada(request):

