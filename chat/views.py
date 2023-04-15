from django.shortcuts import render, redirect


def chat_room(request):
    if request.user.is_authenticated:
        return render(request, 'chat/chat.html')
    else:
        return redirect('login')