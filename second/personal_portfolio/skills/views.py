from .models import Skills, Portfolio
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

def index(request):
    projects = Skills.objects.all()
    return render(request, 'skills/index.html', {'projects': projects})


def portfolio(request):
    porto = Portfolio.objects.all()
    return render(request, 'skills/portfolio.html', {'porto': porto})

def home(request):
    return render(request, 'todo/home.html')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'skills/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'skills/loginuser.html', {'form': AuthenticationForm(), 'error': 'Неверные дванные для входа'})
        else:
            login(request, user)
            return redirect('currenttodos')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'skills/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'skills/signupuser.html',
                              {'form': UserCreationForm(),
                               'error':'Такое имя пользователя уже существует.Задайте другое'})
        else:
            return render(request, 'skills/signupuser.html',
                          {'form': UserCreationForm(),
                           'error': 'Пароли не совпадают'})


def currenttodos(request):
    return render(request, 'skills/currenttodos.html')