from django.shortcuts import render, redirect
from .models import Card


def projects(request):
    pr = Card.objects.all()
    context = {'projects': pr}
    return render(request, 'album/projects.html', context)
