from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),
    path('especialistas/', include('especialistas.urls')),
    path('atividades/', include('atividades_interativas.urls')),
    path('biblioteca/', include('biblioteca.urls')),
    path('noticias/', include('noticias.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
