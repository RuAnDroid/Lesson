from django.shortcuts import render
from .models import Skills,Portfolio


def index(request):
    projects = Skills.objects.all()
    return render(request, 'skills/index.html', {'projects': projects})


def portfolio(request):
    porto = Portfolio.objects.all()
    return render(request, 'skills/portfolio.html', {'porto': porto})
