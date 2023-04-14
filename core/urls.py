from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("translator.urls")),
    path('accounts/', include('accounts.urls')),
    # path('accounts/', include('allauth.urls')),
    path('stori/', include('stori.urls')),

]
