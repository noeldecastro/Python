from django.shortcuts import render
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Avatar
from .forms import NuestraCreacionUser, PasswordEditForm, AvatarForm, DatosEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView



def login(request):


    if request.method == 'POST':
        form  = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username = username, password = password)

            if user is not None:
                django_login(request, user)
                return render(request, 'indice/index.html', {'msj': username})
            else: 
                return render(request, 'accounts/login.html', {'form': form, 'msj': 'No se autentico'})
        else:
            return render(request, 'accounts/login.html', {'form': form, 'msj': 'Datos incorrectos'})
    else: 
        form = AuthenticationForm()            
        return render(request, 'accounts/login.html', {'form' : form})

def registrar(request):

    if request.method == 'POST':
        form = NuestraCreacionUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'indice/index.html', {'msj_registro': f'Se creo el usuario {username}'})
    else:
        form = NuestraCreacionUser()
    return render(request, 'accounts/registrar.html',{'form': form})



def editarContraseña(request):
    user= request.user

    if request.method == 'POST':
        form = PasswordEditForm(request.POST, request.FILES)
        msj = ''
        if form.is_valid():
            informacion = form.cleaned_data
            print(f'Informacion: {informacion}')

            password1 = informacion.get('password1')
            password2 = informacion.get('password2')
            if password1 == password2 and len(password1) > 8:
                user.set_password(password1)
                
            else:
                msj += 'No se modificó el password'
            user.save()
            msj += f'Se modifico la contraseña {user}'
            return render(request, 'indice/index.html',{'msj': msj,"user_avatar_url":buscar_url_avatar(request.user)})
    else:
        form= PasswordEditForm(initial={ 'email':user.email})
    
    return render(request, 'accounts/editarContraseña.html', {'form':form, 'usuario':user,"user_avatar_url":buscar_url_avatar(request.user)})


def agregar_avatar(request):
    form = AvatarForm(request.POST, request.FILES)
    if form.is_valid():
        avatar = Avatar(user=request.user, imagen = form.cleaned_data["imagen"])
        avatar.save()

        return render(request, 'indice/index.html',{"user_avatar_url":buscar_url_avatar(request.user)})
    else:
        form = AvatarForm()
    
    return render(request, 'accounts/agregarAvatar.html',{"form":form,"user_avatar_url":buscar_url_avatar(request.user)})

@login_required
def editarDatos(request):
    request.user
    if request.method == 'POST':
        form = DatosEditForm(request.POST)
        msj = ''
        if form.is_valid():

            data = form.cleaned_data
            request.user.first_name=data.get('first_name', '')
            request.user.last_name=data.get('last_name', '')
            request.user.email=data.get('email', '')

            request.user.save()
            msj += f'Se modificaron sus datos'
            return render(request, 'indice/index.html',{'form':form,'msj': msj,"user_avatar_url":buscar_url_avatar(request.user)})
    else:
        form= DatosEditForm()
    
    return render(request, 'accounts/editarDatos.html', {'form':form,"user_avatar_url":buscar_url_avatar(request.user)})



class Perfil(DetailView):
    model = User
    template_name = 'accounts/perfil.html'



#######################################################################################################################
####################################    No es un view, es una fn que se ejecuta    ####################################
#################################### para enviar la url de los avatars a los views ####################################
#######################################################################################################################
def buscar_url_avatar(user):
    try:
        user_avatars = Avatar.objects.filter(user=user)
        avatar_url = user_avatars[len(user_avatars)-1].imagen.url
    except Exception:
        avatar_url = '/media/avatares/noavatar.jpg'
    finally:
        print(avatar_url)
        return avatar_url
