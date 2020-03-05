
from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    edad = forms.IntegerField()
    nombre = forms.CharField()
    direccion = forms.CharField()
    telefono = forms.CharField()
    observaciones = forms.CharField()
    correo = forms.EmailField()

    class Meta:
        model = Estudiante
        fields = ('nombre','edad','direccion','telefono','observaciones','correo')

