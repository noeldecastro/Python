from dataclasses import fields
from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NuestraCreacionUser(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Constrasena', widget = forms.PasswordInput)
    password2 = forms.CharField(label= 'Repetir Contrasena', widget = forms.PasswordInput)

    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email' , 'password1' , 'password2', 'first_name', 'last_name']
        help_texts = { k: '' for k in fields }

class DatosEditForm(forms.Form):
    first_name = forms.CharField(label = 'Nombre')
    last_name = forms.CharField(label= 'Apellido')
    email = forms.EmailField()

class PasswordEditForm(forms.Form):
    password1 = forms.CharField(label = 'Constraseña', widget = forms.PasswordInput)
    password2 = forms.CharField(label= 'Repetir Contraseña', widget = forms.PasswordInput)

class AvatarForm(forms.Form):
    imagen = forms.ImageField()