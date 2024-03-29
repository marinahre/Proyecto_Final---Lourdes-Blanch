from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User

from django.contrib.auth.views import PasswordChangeView, LogoutView

 

from django.views.generic import DeleteView

 

from django.shortcuts import render, redirect

from django.urls import reverse_lazy

 

from accounts import forms

from accounts import models
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = forms.RegistroUsuarioForm(data=request.POST)
        if form.is_valid():
              form.save()
              return redirect('login')
        else:
            return render(request, 'accounts/crear_acc.html', {'formulario':form})
    form = forms.RegistroUsuarioForm()
    return render(request, 'accounts/crear_acc.html', {'formulario':form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return redirect('Inicio')
            else:
                return render(request, 'accounts/iniciar_sesion.html', {"mensaje":"Datos incorrectos."})
            
    form = AuthenticationForm()
    return render(request, 'accounts/iniciar_sesion.html', {'formulario':form})

def editar_perfil(request):
    usuario = request.user
    modelo_perfil, _ =models.Account.objects.get_or_create(user=usuario)
    if request.method == 'POST':
        form = forms.EditarUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if data.get('email'):
                usuario.email = data.get('email')
            if data.get('first_name'):
                usuario.first_name = data.get('first_name')
            if data.get('last_name'):
                usuario.last_name = data.get('last_name')  

            modelo_perfil.save()
            usuario.save()
            return redirect('Inicio')
        else:
            return render(request, 'accounts/editar_acc.html', {'form':form})
    
    form = forms.EditarUsuarioForm(
        initial={
            'email':usuario.email,
            'first_name':usuario.first_name,
            'last_name':usuario.last_name,
        }
    )
    return render(request, 'accounts/editar_acc.html', {'form':form})

def mostrar_perfil(request):
    return render(request, 'accounts/mostrar_acc.html')

def eliminar_perfil(request):
    pass

def cambiar_password(request):
    pass

class Logout(LogoutView):
    template_name = 'accounts/logout_account.html'