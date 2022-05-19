
from .views import  inicio, infoSalud, contacto, sobrenosotros
from django.urls import path, include

urlpatterns = [
    path('', inicio, name = "inicio"),
    path('infoSalud/', infoSalud, name = "infoSalud"),
    path('contacto/', contacto, name = "contacto"),
    path('sobrenosotros/', sobrenosotros, name = "sobrenosotros")
]