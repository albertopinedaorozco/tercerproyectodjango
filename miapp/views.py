from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import EstudianteForm

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required


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
@login_required
def listar_asignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(request,'miapp/asignaturas.html', {'lista_asignaturas': asignaturas})

def listar_programas(request):
    programas = Programa.objects.all()
    return render(request,'miapp/programas.html', {'lista_programas': programas})

def estudiante_detalle(request,id):
    estudiante = Estudiante.objects.get(id=id)
    return render(request,'miapp/estudiante_detalle.html',{'estudiante': estudiante})

def estudiante_nuevo(request):

    if request.method == 'GET':
        formu = EstudianteForm()
        return render(request, 'miapp/estudiante_nuevo.html', {'form': formu})
    else:
        formu = EstudianteForm(request.POST)
        if formu.is_valid():
            formu.save()
            return redirect('index_n')

def estudiante_borrar(request, id):
    estudiante = Estudiante.objects.get(id=id)
    return render(request,'miapp/estudiante_eliminar.html', {'estudiante': estudiante})

def estudiante_borrar_confirmar(request, id):
    estudiante = Estudiante.objects.get(id=id)
    estudiante.delete()
    return redirect('index_n')

def estudiante_actualizar(request, id):
    estudiante = Estudiante.objects.get(id=id)
    if request.method == 'GET':
        
        formu = EstudianteForm(instance=estudiante)
        return render(request, 'miapp/estudiante_actualizar.html', {'form': formu})
    else:
        formu = EstudianteForm(request.POST, instance=estudiante)
        formu.save()
        return redirect('index_n')


    




