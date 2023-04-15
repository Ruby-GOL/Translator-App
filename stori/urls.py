from django.urls import path

from . import views

urlpatterns = [
    path('', views.stori, name='stori'),
    path('<slug:slug>/', views.stori, name='stori'),
]
