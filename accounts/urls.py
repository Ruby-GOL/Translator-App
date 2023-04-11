"""Django imports"""
from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

""" Local Imports"""

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name="logout"),

    path("auth/login/", LoginView.as_view
         (template_name="chat/LoginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]
