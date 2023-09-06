from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import curso
from .models import estudiantes
from .models import profesores


def inicio(request):
    return render(request ,"AppCoder/inicio.html")


def cursos_view(request):
    if request.method == "GET":
        return render(request , "AppCoder/curso_formulario.html",)
    
    else:
        print(request.POST)

        modelo_cursos=curso(curso=request.POST["curso"], camada=request.POST["camada"])
        modelo_cursos.save()
        return render(request , "AppCoder/inicio.html",)
    
   

def estudiantes_view(request):
    if request.method == "GET":
        return render(request , "AppCoder/estudiantes.html",)
    
    else:
        print(request.POST)

    modelo_estudiantes=estudiantes(nombre=request.POST["nombre"], apellido=request.POST["apellido"], email=request.POST["email"])
    modelo_estudiantes.save()
    return render(request , "AppCoder/inicio.html",)
    


def profesores_view(request):
    if request.method == "GET":
        return render(request , "AppCoder/profesores.html",)
    
    else:
        print(request.POST)

    modelo_profesores=profesores(nombre=request.POST["nombre"], apellido=request.POST["apellido"], profesion=request.POST["profesion"],  email=request.POST["email"])
    modelo_profesores.save()
    return render(request , "AppCoder/inicio.html",)
    