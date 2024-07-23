# news/views.py
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import login as login_django
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Noticias
from .forms import NoticiasForm
#from pyexpat.errors import messages



@login_required
def listanoticias(request):
    noticia = Noticias.objects.all()
    return render(request, 'noticias/lista.html', {'noticia': noticia})


@login_required
def detalhesnoticias(request, pk):
    noticia = get_object_or_404(Noticias, pk=pk)
    return render(request, 'noticias/detalhesnoticia.html', {'noticia': noticia})


@login_required
@user_passes_test(lambda u: u.is_staff)
def createnoticias(request):
    if request.method == 'POST':
        form = NoticiasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listanoticias')
    else:
        form = NoticiasForm()
    return render(request, 'noticias/createnoticia.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.is_staff)
def updatenoticias(request, pk):
    #if request.user.groups.filter(name='administrador').exists():
    noticia = get_object_or_404(Noticias, pk=pk)
    if request.method == 'POST':
        form = NoticiasForm(request.POST,request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('listanoticias')
    else:
        form = NoticiasForm(instance=noticia)
    return render(request, 'noticias/updatenoticias.html', {'form': form, 'noticia': noticia})

#else:
   # return render(request, {'message': 'Você não tem permissão para acessar esta página.'})


@login_required
@user_passes_test(lambda u: u.is_staff)
def deletenoticias(request, pk):
    noticia = get_object_or_404(Noticias, pk=pk)
    if request.method == 'POST':
        noticia.delete()
        return redirect('listanoticias')
    return render(request, 'noticias/confirmdeletenoticia.html', {'noticia': noticia})

#else:
    #return render(request, {'message': 'Você não tem permissão para acessar esta página.'})