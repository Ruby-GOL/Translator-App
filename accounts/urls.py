"""Django imports"""
from django.urls import path

""" Local Imports"""
from . import views

urlpatterns = [
    path('register/',views.register, name="register"),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name="logout"),
    path('contact/', views.contact, name='contact'),
       
       
]