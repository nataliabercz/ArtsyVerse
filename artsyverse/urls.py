from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from artsyverse import settings

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)