from django.urls import path
from . import views

urlpatterns = [
    path('', views.translate, name='index'),
]


# Path: txt2sp/views.py