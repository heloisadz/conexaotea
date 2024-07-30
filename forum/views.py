from pyexpat.errors import messages
from urllib import request
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import login as login_django
from django.contrib.auth import logout
from django.shortcuts import redirect
from forum.forms import ForumForm
from usuario.models import Usuario # type: ignore
from .models import Forum
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
def createpost(request):
    if request.method == 'POST':
        form = ForumForm(request.POST, user=request.user)  # Passe o usuário aqui
        if form.is_valid():
            form.save()
            return redirect('/forum/')
    else:
        form = ForumForm(user=request.user)  # Passe o usuário aqui
    return render(request, 'forum/createpost.html', {'form': form})
    
@login_required
def forum(request):
    forum = Forum.objects.all()
    return render(request, 'forum/home.html', {'forum': forum})
    #raise Http404("vC NÃO TEM permissão para acessar aqui.")

#fltou mexer daq pra baixo
@login_required
def updatepost(request, forum_id):
    forum = get_object_or_404(Forum, pk=forum_id)
    
    # Verificar se o usuário que está tentando editar é o autor do post
    if request.user == forum.user:
        if request.method == 'POST':
            form = ForumForm(request.POST, instance=forum)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/forum/")
        else:
            form = ForumForm(instance=forum)
        return render(request, 'forum/updatepost.html', {'form': form, 'forum_id': forum_id})
    else:
        return render(request, 'error.html', {'message': 'Você não tem permissão para acessar esta página.'})

@login_required
def deletepost(request, forum_id):
    forum = get_object_or_404(Forum, pk=forum_id)
    
    # Verificar se o usuário que está tentando deletar é o autor do post
    if request.user == forum.user:
        forum.delete()
        return HttpResponseRedirect('/forum/')
    else:
        return render(request, 'error.html', {'message': 'Você não tem permissão para acessar esta página.'})

@login_required
def confirmDelete(request, forum_id):

    forum = get_object_or_404(Forum, id=forum_id)
    if request.user == forum.user:
        forum = get_object_or_404(Forum, pk=forum_id)
        return render(request, 'forum/confirmdeletepost.html', {'forum': forum})
    else:
        return render(request, 'error.html', {'message': 'Você não tem permissão para acessar esta página.'})
    


