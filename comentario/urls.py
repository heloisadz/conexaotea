from django.urls import path
from . import views
from .models import Forum
urlpatterns = [
    path('', views.comentario, name ='comentario'),
    path('createcomentario/<int:forum_id>/', views.createcomentario, name='createcomentario'),
    path('updatecomentario/<int:comentario_id>', views.updatecomentario, name="updatecomentario"),
    path('deletecomentario/<int:comentario_id>', views.deletecomentario, name="deletecomentario"),
    path('delete/confirm/<int:comentario_id>', views.confirmDelete, name="confirmdelete"),
    path('<int:forum_id>/', views.detail, name='detail'),
    
]
   
