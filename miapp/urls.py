from django.urls import path, include
from .views import *

urlpatterns = [
    path('',  listar_estudiantes, name='index_n'),
    path('docentes/',  listar_docentes, name='docentes_n' ),
    path('asignaturas/',  listar_asignaturas, name ='asignaturas_n'),
    path('programas/',  listar_programas, name='programas_n'),
    path('estudiante/detalle/<int:id>',  estudiante_detalle, name='estudiante_detalle_n'),
       
]