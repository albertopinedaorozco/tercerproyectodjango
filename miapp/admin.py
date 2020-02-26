from django.contrib import admin

from .models import Estudiante, Asignatura, Docente, Programa

admin.site.register(Estudiante)
admin.site.register(Asignatura)
admin.site.register(Programa)
admin.site.register(Docente)
