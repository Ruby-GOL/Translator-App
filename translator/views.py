from django.shortcuts import render, redirect

# Create your views here.


def homepage(request):
    return render(
        request=request,
        template_name='index.html')


def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat/chatPage.html", context)
