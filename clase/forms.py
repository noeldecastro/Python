from unittest.util import _MAX_LENGTH
from django import forms
from ckeditor.fields import RichTextField
from datetime import datetime

class PacienteFormulario(forms.Form):
    nombre = forms.CharField(max_length = 20)
    apellido = forms.CharField(max_length = 25)
    email = forms.EmailField()

class BusquedaDoctor(forms.Form):
    partial_doctor = forms.CharField(label = 'Nombre doctor', max_length = 20)

class TurnoFormulario(forms.Form):
    # doctor = forms.CharField(label= 'Seleccion su medico:', widget= forms.Select(Doctor.objects))
    fechaTurno = forms.DateTimeField(
        input_formats = ['%Y-%m-%dT%H:%M'],
        widget = forms.DateTimeInput(
        attrs={
            'type': 'datetime-local',
            'class': 'form-control'},
        format='%Y-%m-%dT%H:%M')
    )

class BlogForm(forms.Form):
    Imagen = forms.ImageField()

