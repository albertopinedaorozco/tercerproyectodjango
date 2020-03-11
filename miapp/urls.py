from django.urls import path, include
from .views import *

urlpatterns = [
    path('',  listar_estudiantes, name='index_n'),
    path('docentes/',  listar_docentes, name='docentes_n' ),
    path('asignaturas/',  listar_asignaturas, name ='asignaturas_n'),
    path('programas/',  listar_programas, name='programas_n'),
    path('estudiante/detalle/<int:id>',  estudiante_detalle, name='estudiante_detalle_n'),
    path('estudiante/borrar/<int:id>',  estudiante_borrar, name='estudiante_borrar_n'),
    path('estudiante/borrar/<int:id>/confirmar',  estudiante_borrar_confirmar, name='estudiante_borrar_confirma_n'),
    path('estudiante/nuevo',  estudiante_nuevo, name='estudiante_nuevo_n'),
    path('estudiante/actualizar/<int:id>',  estudiante_actualizar, name='estudiante_actualizar_n'),
    path('iniciosesion/', LoginView.as_view(template_name='accounts/login.html') , name='login'),
    path('cerrarsesion/', LogoutView.as_view(template_name='accounts/logout.html') , name='logout'),
       
]