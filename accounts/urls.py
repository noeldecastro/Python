from clase import views
from .views import editarContraseña, login, registrar, agregar_avatar, editarDatos
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views   

urlpatterns = [
    path('login/', login, name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'indice/index.html') , name = 'logout'),
    path('registrar/', registrar, name = 'registrar'),
    path('perfil/<pk>', views.Perfil.as_view(), name = 'Perfil'),
    path('agregarAvatar/',agregar_avatar, name='agregarAvatar'),
    path('editarContraseña/',editarContraseña, name='editarContraseña'),
    path('editarDatos/',editarDatos, name='editarDatos')
]