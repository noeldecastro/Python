from django.urls import path
from .views import actualizar_turno, busqueda_doctor, formulario_paciente,  nuevo_doctor, formulario_turno
from . import views

urlpatterns = [
    #Doctor
    path('nuevo_doctor/', nuevo_doctor, name = 'nuevo_doctor'),
    path('busqueda-doctor/', busqueda_doctor, name = 'busqueda_doctor'),

    #Paciente
    path('paciente/', formulario_paciente, name = 'formulario_paciente'),

    #Turno
    path('turnos/', views.TurnoLista.as_view(), name = 'List'),
    path(r'^(?P<pk>\d+)$', views.TurnoDetalle.as_view(), name = 'Detail'),
    path(r'^borrar/(?P<pk>\d+)$', views.TurnoDelete.as_view(), name = 'Delete'),
    path('actualizar_turno/<int:id>', actualizar_turno, name = 'EditTurno'),
    path('nuevo_turno/', formulario_turno, name = 'nuevo_turno'),

    #Blog
    path('nuevo_blog/', views.BlogCreacion.as_view(), name = 'NewBlog'),
    path('blog/', views.BlogLista.as_view(), name = 'BlogList'),
    path('^editar/<pk>', views.BlogUpdate.as_view(), name = 'EditBlog'),
    path('<pk>', views.BlogDetalle.as_view(), name = 'BlogDetail'),
    path(r'^borrarBlog/(?P<pk>\d+)$', views.BlogDelete.as_view(), name = 'BlogDelete')
]