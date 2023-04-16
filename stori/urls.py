from django.urls import path

from . import views

urlpatterns = [
    path('', views.stori, name='chat'),
    path('<slug:slug>/', views.stori, name='chat'),
]
