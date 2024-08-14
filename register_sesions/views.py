from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from register_sesions.forms import PlayerForm
from .models import Player

def save_player(request):

    if request.method == 'POST':
        mail = request.POST.get('mail')
        name = request.POST.get('name')
        password = request.POST.get('password')

        # Creando el usuario en la BD
        user = User(username = mail, password = password)
        user.set_password(password)  # Encripta el password
        user.save()

        # Creando el jugador en la BD
        player = Player(mail = mail, name = name, user = user)
        player.save()

        return redirect('login')
    else:
        return HTTPResponse('No se recibieron datos')
    

def login_view(request):
    context = {}
    form = PlayerForm()
    context['form'] = form
    return render(request, 'login/login.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

