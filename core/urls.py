from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("translator.urls")),
    path('accounts/', include('accounts.urls')),
    # path('accounts/', include('allauth.urls')),
    path('chat/', include('stori.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

