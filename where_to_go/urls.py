from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from places.views import show_place, show_point


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_point),
    path('places/<int:id>/', show_place, name='place'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
