from django.urls import path
from . import views

urlpatterns = [
    path('/translator', views.index, name='index'),
    path("", views.homepage, name='home'),

]
