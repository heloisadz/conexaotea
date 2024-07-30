from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import login as login_django
from django.contrib.auth import logout
from django.shortcuts import redirect
from comentario.forms import ComentarioForm
import forum
from usuario.models import Usuario # type: ignore
from .models import Comentario, Forum
from django.contrib.auth.models import Group
from forum.models import Forum  # Certifique-se de importar o modelo Forum
from .forms import ComentarioForm

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

# comentario/views.py


@login_required
def createcomentario(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)  # Obtém o fórum pelo ID

    if request.method == 'POST':
        form = ComentarioForm(request.POST)  # Cria o formulário com os dados POST
        if form.is_valid():
            comentario = form.save(commit=False)  # Não salva imediatamente
            comentario.user = request.user  # Associa o usuário logado
            comentario.forum = forum  # Associa o fórum ao comentário
            comentario.save()  # Salva o comentário
            return redirect('detail', forum_id=forum_id)  # Redireciona para a página de detalhes do fórum
    else:
        form = ComentarioForm()  # Cria um formulário vazio para GET

    return render(request, 'comentario/createcomentario.html', {'form': form, 'forum': forum})

@login_required
def detail(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    comentario = Comentario.objects.filter(forum=forum)  # Corrija o nome do campo aqui
    return render(request, 'comentario/detail.html', {'comentario': comentario, 'forum': forum})


@login_required
def comentario(request):
    comentario = Comentario.objects.all()
    return render(request, 'comentario/<int:forum_id>/', {'comentario': comentario})
    #raise Http404("vC NÃO TEM permissão para acessar aqui.")

#fltou mexer daq pra baixo
@login_required
def updatecomentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id)
    
    # Verificar se o usuário que está tentando editar é o autor do post
    if request.user == comentario.user:
        if request.method == 'POST':
            form = ComentarioForm(request.POST, instance=comentario)
            if form.is_valid():
                form.save()
                # Aqui, certifique-se de passar uma lista ou queryset para 'comentarios'
                return render(request, 'comentario/detail.html', {'comentario': [comentario], 'forum': comentario.forum})
        else:
            form = ComentarioForm(instance=comentario)
        return render(request, 'comentario/updatecomentario.html', {'form': form, 'comentario_id': comentario_id})
    else:
        return render(request, 'error.html', {'message': 'Você não tem permissão para acessar esta página.'})


@login_required
def confirmDelete(request, comentario_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id)
    
    if request.user == comentario.user:
        return render(request, 'comentario/confirmdeletecomentario.html', {'comentario': comentario})
    else:
        return render(request, 'error.html', {'message': 'Você não tem permissão para acessar esta página.'})

@login_required
def deletecomentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id)
    
    # Verificar se o usuário que está tentando deletar é o autor do post
    if request.user == comentario.user:
        comentario.delete()
        return redirect('detail', forum_id=comentario.forum.id)  # Corrigido o redirecionamento
    else:
        return render(request, 'error.html', {'message': 'Você não tem permissão para acessar esta página.'})
