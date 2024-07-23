# news/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listanoticias, name='listanoticias'),
    path('noticias/<int:pk>/', views.detalhesnoticias, name='detalhesnoticias'),
    path('noticias/createnoticias/', views.createnoticias, name='createnoticias'),
    path('noticias/<int:pk>/update/', views.updatenoticias, name='updatenoticias'),
    path('noticias/<int:pk>/delete/', views.deletenoticias, name='deletenoticias'),
]
