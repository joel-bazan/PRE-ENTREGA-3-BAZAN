from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import CursoFormulario, ProfesorFormulario, UserRegisterForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def inicio(request):
    return render (request, 'AppCoder/inicio.html')

    #return HttpResponse("vista inicio")
"""
def cursos(request):
    return render (request, 'AppCoder/cursos.html')

    #return HttpResponse("vista cursos")
"""

def profesores(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], 
                                email=informacion['email'], profesion=informacion['profesion'])
            profesor.save()
            return render(request, "AppCoder/inicio.html")
        
    else:
        miFormulario = ProfesorFormulario()
        
    return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})        

   # return HttpResponse("vista profesores")

def entregables(request):
    return render (request, 'AppCoder/entregables.html')

    #return HttpResponse("vista entregables")

def estudiantes(request):
    return render (request, 'AppCoder/estudiantes.html')

    #return HttpResponse("vista estudiantes")
    
"""def curso(self):
        curso=Curso(nombre="Desarrollo Web"), comision=19881
        curso.save()
        documentoDeTexto=f"--->Curso:{curso.nombre} comision: {curso.comision}
        return HttpResponse(documentoDeTexto)
        
def cursoFormulario(request):
     if request.method=="POST":
          curso=Curso(request.POST['curso'],(request.POST['comision']))
          curso.save()
          return render (request, "AppCoder/inicio.html")
     
     return render(request,"Appcoder/cursoFormulario.html")
"""
def cursos(request):
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

#def busquedacomision(request):

def busquedaComision(request):
    return render(request, "AppCoder/busquedaComision.html")

def buscar(request):
    if request.GET["comision"]:
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains=comision)
        return render(request, "AppCoder/resultadoBusqueda.html", {"cursos":cursos, "comision":comision})
        #return render(request, "AppCoder/inicio.html", {"cursos":cursos, "comision":comision})
    else:
        respuesta = "No enviaste datos" 

    #return render(request, "AppCoder/inicio.html", {"respuesta":respuesta})
    
    #respuesta = f"Estoy buscando la comision nro: {request.GET['comision']}"
    
    return HttpResponse(respuesta)

def leerProfesores(request):
    profesores = Profesor.objects.all()
    contexto = {"profesores": profesores}
    return render(request, "AppCoder/leerProfesores.html", contexto)

def eliminarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
    
    profesores = Profesor.objects.all()
    contexto= {"profesores":profesores}
    return render(request, "AppCoder/leerProfesores.html", contexto)

def editarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre =profesor_nombre)
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido'] 
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']
            
            profesor.save()
            
            return render(request, "AppCoder/inicio.html")
        
    else:
        miFormulario = ProfesorFormulario(initial={'nombre':profesor.nombre, 
                                                   'apellido':profesor.apellido, 
                                                   'email':profesor.email, 
                                                   'profesion': profesor.profesion})
        
    return render(request, "AppCoder/editarProfesor.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})        

class CursoList(ListView):
    model = Curso
    template_name = "AppCoder/cursos_list.html"
    
class CursoDetalle(DetailView):
    model = Curso
    template_name = "AppCoder/curso_detalle.html"
    
class CursoCreacion(CreateView):
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ['nombre', 'comision']

class CursoUpdate(UpdateView):
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ['nombre', 'comision']  
    
class CursoDelete(DeleteView):
    model = Curso
    success_url = "/AppCoder/curso/list"

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCoder/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppCoder/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"form": form})

# Vista de registro
def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})


