from django.shortcuts import render, redirect
from .models import Card
from .utils import search_projects


def projects(request):
    pr, search_query = search_projects(request)
    context = {'projects': pr, 'search_query': search_query}
    return render(request, 'album/projects.html', context)


def login(request):
    return render(request, 'album/login.html')


def contact(request):
    return render(request, 'album/contact.html')


def single_card(request, pk):
    card_obj = Card.objects.get(id=pk)
    return render(request, 'album/single-card.html', {'card': card_obj})


def developers(request):
    return render(request, 'album/developers.html')
