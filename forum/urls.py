from django.urls import path
from . import views
urlpatterns = [
    path('', views.forum, name ='forum'),
    path('createpost/', views.createpost, name ='createpost'),
    path('updatepost/<int:forum_id>', views.updatepost, name="updateespecialista"),
    path('deletepost/<int:forum_id>', views.deletepost, name="deletepost"),
    path('delete/confirm/<int:forum_id>', views.confirmDelete, name="confirmdelete"),
    #path('<int:forum_id>', views.detail, name="detail"),
    
    #path('detail/<int:post_id>/', views.viewpost, name='viewpost')
]
   
