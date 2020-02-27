from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def inicio(request):
    return HttpResponse("Hola mundo")

def contacto(request):
    return HttpResponse("<h1>Contacto</h1>")

def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request,'miapp/index.html', {'lista_estudiantes': estudiantes })


def listar_docentes(request):
    docentes = Docente.objects.all()
    return render(request,'miapp/docentes.html', {'lista_docentes': docentes})

def listar_asignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(request,'miapp/asignaturas.html', {'lista_asignaturas': asignaturas})

def listar_programas(request):
    programas = Programa.objects.all()
    return render(request,'miapp/programas.html', {'lista_programas': programas})

def estudiante_detalle(request,id):
    estudiante = Estudiante.objects.get(id=id)
    return render(request,'miapp/estudiante_detalle.html',{'estudiante': estudiante})



