from django.shortcuts import render


# from indice.forms import NuestraCreacionUser

def inicio(request):
    return render(request, "indice/index.html", {})


def infoSalud(request):
    return render(request, "indice/infoSalud.html",{})


def contacto(request):
    return render(request, "indice/contacto.html",{})


def sobrenosotros(request):
    return render(request, "indice/sobrenosotros.html", {})


