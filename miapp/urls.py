from django.urls import path, include
from .views import *

urlpatterns = [
    path('',  listar_estudiantes),
    path('contacto/',  contacto ),
    path('docentes/',  listar_docentes ),
    path('asignaturas/',  listar_asignaturas),
    path('programas/',  listar_programas),
    
]