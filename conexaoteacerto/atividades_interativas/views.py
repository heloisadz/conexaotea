from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import login as login_django
from django.contrib.auth import logout
from django.shortcuts import redirect
from atividades_interativas.forms import AtividadesForm
from usuario.models import Usuario # type: ignore
from .models import Atividades
from django.contrib.auth.models import Group

#cria especialista novo
#@login_required
#def createespecialista(request):
    # Obtenha o usuário atual
 #   usuario = get_object_or_404(Usuario, username=request.user)
    
    # Verifique se o usuário pertence ao grupo "administrador"
  #  if usuario.groups.filter(name='administrador').exists():
   #     if request.method == 'POST':
    #        form = EspecialistaForm(request.POST)
     #       if form.is_valid():
      #          form.save()
       #         return HttpResponseRedirect("/especialistas/")
        #    else:
         #       form = EspecialistaForm()
          #  return render(request, 'createespecialista.html', {'form': form})
   # else:
    #    return render(request, 'error.html', {'message': 'Você não tem permissão para acessar esta página.'})

@login_required
def createatividade(request):
    if request.user.groups.filter(name='administrador').exists():
        if request.method == 'POST':
            form = AtividadesForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/atividades/")
        else:
            form = AtividadesForm()
        return render(request, 'createatividade.html', {'form': form})
    else:
        return render(request, {'message': 'Você não tem permissão para acessar esta página.'})

@login_required
def atividades(request):
    atividades = Atividades.objects.all()
    return render(request, 'atividades.html', {'atividades': atividades})

@login_required
def readatividades(request):
    atividades = Atividades.objects.all()
    return render(request, 'readatividades.html', {'atividades': atividades})

@login_required
def updateatividade(request, id_atividade):
    if request.user.groups.filter(name='administrador').exists():
        atividades = get_object_or_404(Atividades, pk=id_atividade)
        if request.method == 'POST':
            form = AtividadesForm(request.POST, instance=atividades)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/atividades/")
        else:
            form = AtividadesForm(instance=atividades)
        return render(request, 'updateatividade.html', {'form': form, 'id_atividade': id_atividade})
    else:
        return render(request, 'error.html', {'message': 'Você não tem permissão para acessar esta página.'})

@login_required
def deleteatividade(request, id_atividade):
    if request.user.groups.filter(name='administrador').exists():
        atividade = get_object_or_404(Atividades, pk=id_atividade)
        atividade.delete()
        return HttpResponseRedirect('/atividades/')
    else:
        return render(request, 'error.html', {'message': 'Você não tem permissão para acessar esta página.'})

@login_required
def confirmDelete(request, id_atividade):
    if request.user.groups.filter(name='administrador').exists():
        atividade = get_object_or_404(Atividades, pk=id_atividade)
        return render(request, 'confirmdeleteatividade.html', {'atividades': atividade})
    else:
        return render(request, 'error.html', {'message': 'Você não tem permissão para acessar esta página.'})