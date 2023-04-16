"""Django imports"""
from django.urls import path

""" Local Imports"""
from . import views

urlpatterns = [
    # path('register/',views.register, name="register"),
    # path('login/', views.login_request, name='login'),
    path('register/patient/', views.patient_registration, name='patient_registration'),
    path('register/doctor/', views.doctor_registration, name='doctor_registration'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_request, name="logout"),

          
]