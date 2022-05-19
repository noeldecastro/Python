
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from clase.models import Paciente, Doctor, Turno, Blog
from clase.forms import PacienteFormulario, BusquedaDoctor, TurnoFormulario, BlogForm
from django.contrib.auth.decorators import login_required
#Para clases basadas en vista
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



#Doctor
def nuevo_doctor(request):
    nuevo_doctor = Doctor(nombre = 'Jorge', apellido = 'apellido', email = 'jorge@gmail.com', profesion = 'Cardiologo')
    nuevo_doctor.save()
    return HTTPResponse(f"Doctor: {nuevo_doctor.apellido},{nuevo_doctor.nombre}")

def busqueda_doctor(request):

    doctores_buscados = []
    dato = request.GET.get('partial_doctor', None)
    if dato is not None:
        doctores_buscados = Doctor.objects.filter(nombre__icontains = dato)
        
    buscador = BusquedaDoctor()

    return render(
        request, "clase/busqueda_doctor.html", 
        {'buscador': buscador,'doctores_buscados': doctores_buscados, 'dato': dato}
        )

#Paciente
def formulario_paciente(request):
    if request.method == 'POST':
        formulario = PacienteFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_curso = Paciente(nombre = data['nombre'], apellido = data['apellido'], email = data['email'])
            nuevo_curso.save()
            return redirect('formulario_paciente')
    else: 
        formulario = PacienteFormulario()
    return render(request, 'clase/formulario_paciente.html', {'formulario': formulario})


#Turno
@login_required
def formulario_turno(request):
    if request.method == 'POST':
        formulario = TurnoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_turno = Turno(fechaTurno = data['fechaTurno'], atendido = False)
            nuevo_turno.save()
            return redirect('List')
    else: 
        formulario = TurnoFormulario()
    return render(request, 'clase/formulario_turno.html', {'formulario': formulario})


def actualizar_turno(request, id):
    turno = Turno.objects.get(id = id)
    if request.method == 'POST':
        formulario = TurnoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            turno.fechaTurno = data['fechaTurno']
            turno.save()
            return redirect('List')
    else:
        formulario = TurnoFormulario(initial = { 'fecha': Turno.fechaTurno, 'Estado': Turno.atendido})
    return render(request, 'clase/actualizar_turno.html', {'formulario': formulario , 'turno':turno})



#Clases basadas en vistas:
#Turno
class TurnoLista(ListView):
    model = Turno
    template_name = 'clase/turno_list.html'


class TurnoDetalle(DetailView):
    model = Turno
    template_name = 'clase/turno_detalle.html'


class TurnoDelete(DeleteView):
    model=Turno
    success_url= '/turnos/'

#Blog
class BlogLista(ListView):
    model = Blog
    template_name = 'clase/blog_list.html'

class BlogCreacion(CreateView):
    model = Blog
    template_name = 'clase/blog_form.html'
    success_url = '/blog/'
    fields = ["titulo", "subtitulo", "contenido", "Autor", "Imagen", "Fecha"]


class BlogUpdate(UpdateView):
    model=Blog
    template_name = 'clase/blog_form.html'
    success_url= '/blog/'
    fields = ["titulo", "subtitulo", "contenido", "Autor", "Imagen", "Fecha"]

class BlogDetalle(DetailView):
    model = Blog
    template_name = './clase/blog_detalle.html'

class BlogDelete(DeleteView):
    model=Blog
    success_url= '/blog/'
