from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),
    path('especialistas/', include('especialistas.urls')),
    path('atividades/', include('atividades_interativas.urls')),
    path('biblioteca/', include('biblioteca.urls')),
]
