from django.urls import path
from . import views
urlpatterns = [
    path('', views.atividades, name ='atividades'),
    path('readatividades/', views.readatividades, name ='readatividades'),
    path('createatividade/', views.createatividade, name ='createatividade'),
    path('updateatividade/<int:id_atividade>', views.updateatividade, name="updateatividade"),
    path('deleteatividade/<int:id_atividade>', views.deleteatividade, name="deleteatividade"),
    path('delete/confirm/<int:id_atividade>', views.confirmDelete, name="confirmdelete"),
]
