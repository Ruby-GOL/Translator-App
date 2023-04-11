from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from translator import views as trans

urlpatterns = [
    path("home", views.homepage, name='home'),
    path("", trans.chatPage, name="chat-page"),
    path("auth/login/", LoginView.as_view
         (template_name="chat/LoginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),

]
