from django.urls import path
from . import views

urlpatterns = [
    path('translator/', views.index, name='translator'),
    path("", views.landing_page, name='landing'),
    path("about/", views.about, name='about'),
    path("home/", views.homepage, name='home'),
    path("services/", views.services, name='services'),
]
