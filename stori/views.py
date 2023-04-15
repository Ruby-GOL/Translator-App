from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room, Message


@login_required
def stori(request):
    rooms = Room.objects.all()

    return render(request, 'stori/rooms.html', {'rooms': rooms})


@login_required
def stori(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'stori/room.html', {'room': room, 'messages': messages})
