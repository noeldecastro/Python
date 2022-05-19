from django.contrib import admin

from .models import Doctor, Paciente, Turno

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(Turno)