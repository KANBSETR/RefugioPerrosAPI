from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import PerroForm
from .models import Perro
# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('refugio')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })


def listar_perros(request):
    perros = Perro.objects.all()
    return render(request, 'refugio.html', {'perros': perros})

def cerrar_sesion(request):
    logout(request)
    return redirect('home')


def inicioSesion(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('refugio')

def agregarPerro(request):
    if request.method == 'GET':
        return render(request, 'agregarPerro.html', {
            'form': PerroForm})
    else:
        try:
            form = PerroForm(request.POST)
            newPerro = form.save(commit=False)
            newPerro.user = request.user
            newPerro.save()
            return redirect('refugio')
        except ValueError:
            return render(request, 'agregarPerro.html', {
                'form': PerroForm,
                'error': 'Error al guardar el perro'
            })
def refugio(request):
    return render(request, 'refugio.html')

def perro_detail(request, perro_id):
    if request.method == 'GET':
        perro = get_object_or_404(Perro, pk=perro_id)
        form = PerroForm(instance=perro)
        return render(request, 'perro_details.html', {'perro': perro, 'form': form})
    else:
        try:
            perro = get_object_or_404(Perro, pk=perro_id)
            form = PerroForm(request.POST, instance=perro)
            form.save()
            return redirect('refugio')
        except ValueError:
            return render(request, 'perro_details.html', {
                'perro': perro,
                'form': form,
                'error': 'Error al guardar el perro'
            })

    
def perro_delete(request, perro_id):
    perro = get_object_or_404(Perro, pk=perro_id, user=request.user)
    if request.method == 'POST':
        perro.delete()
        return redirect('refugio')