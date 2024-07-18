from django.urls import path
from . import views
urlpatterns = [
    path('', views.biblioteca, name ='biblioteca'),
    path('readbiblioteca/', views.readbiblioteca, name ='readbiblioteca'),
    path('createbiblioteca/', views.createbiblioteca, name ='createbiblioteca'),
    path('updatebiblioteca/<int:id_biblioteca>', views.updatebiblioteca, name="updatebiblioteca"),
    path('deletebiblioteca/<int:id_biblioteca>', views.deletebiblioteca, name="deletebiblioteca"),
    path('delete/confirm/<int:id_biblioteca>', views.confirmDelete, name="confirmdelete"),
]
