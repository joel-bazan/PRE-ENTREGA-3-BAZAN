from django.urls import path
from AppCoder import views
#from AppCoder import curso
#views

urlpatterns = [
    path('', views.inicio,name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    #path('cursoFormulario', views.cursoFormulario, name="cursoFormulario"),
    path('busquedaComision', views.busquedaComision, name="BusquedaComision"),
    path('buscar/', views.buscar)
]