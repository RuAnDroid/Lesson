from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Room, Message


@login_required
def room(request, id):
    room = get_object_or_404(Room, id=id)
    return render(request, 'porto/room.html', {'room': room})

@login_required
def send_message(request, id):
    room = get_object_or_404(Room, id=id)
    return render(request, 'porto/room.html', {'room': room})
