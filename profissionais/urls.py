from django.urls import path
from . import views
urlpatterns = [
    path('profissionais/', views.profissionais, name ='profissionais'),
    path('createprofissionais/', views.createprofissionais, name ='createprofissionais'),
   
]