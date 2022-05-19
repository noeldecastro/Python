from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=25)
    email = models.EmailField()
    def __str__(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido}"


class Doctor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=25)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido}"


class Turno(models.Model):
    fechaTurno = models.DateTimeField()
    atendido = models.BooleanField()
    def __str__(self):
        return f"Fecha: {self.fechaTurno} Estado: {self.atendido}"

class Blog(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=25)
    contenido = RichTextField(null=True, blank = True)
    Autor = models.CharField(max_length=30)
    Imagen = models.ImageField(upload_to='media/blog', null=True, blank=True)
    Fecha = models.DateField(default = timezone.now)
