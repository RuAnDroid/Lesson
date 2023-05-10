from django.shortcuts import render, redirect
from .models import Card
from .utils import search_projects
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .forms import CustomUserCreationForm


def projects(request):
    pr, search_query = search_projects(request)
    context = {'projects': pr, 'search_query': search_query}
    return render(request, 'album/projects.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('projects')

    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('projects')
        else:
            messages.error(request, "Username or password is incorrect")

    return render(request, 'album/login_register.html')


def logout_user(request):
    logout(request)
    messages.info(request, "User was logged out!")
    return redirect('login')


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')
            login(request, user)
            return redirect('projects')
        else:
            messages.error(request, 'An error has occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'album/login_register.html', context)

def contact(request):
    return render(request, 'album/contact.html')


def single_card(request, pk):
    card_obj = Card.objects.get(id=pk)
    return render(request, 'album/single-card.html', {'card': card_obj})


def developers(request):
    return render(request, 'album/developers.html')
