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
from biblioteca.forms import BibliotecaForm
from usuario.models import Usuario # type: ignore
from .models import Biblioteca
from django.contrib.auth.models import Group

@login_required
def createbiblioteca(request):
    if request.user.groups.filter(name='administrador').exists():
        if request.method == 'POST':
            form = BibliotecaForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/biblioteca/")
        else:
            form = BibliotecaForm()
        return render(request, 'biblioteca/createbiblioteca.html', {'form': form})
    else:
        return render(request, {'message': 'Você não tem permissão para acessar esta página.'})

@login_required
def biblioteca(request):
    biblioteca = Biblioteca.objects.all()
    return render(request, 'biblioteca/biblioteca.html', {'biblioteca': biblioteca})

@login_required
def readbiblioteca(request):
   biblioteca = Biblioteca.objects.all()
   return render(request, 'biblioteca/readbiblioteca.html', {'biblioteca': biblioteca})

@login_required
def updatebiblioteca(request, id_biblioteca):
    if request.user.groups.filter(name='administrador').exists():
        biblioteca = get_object_or_404(Biblioteca, pk=id_biblioteca)
        if request.method == 'POST':
            form = BibliotecaForm(request.POST, instance=biblioteca)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/biblioteca/")
        else:
            form = BibliotecaForm(instance=biblioteca)
        return render(request, 'biblioteca/updatebiblioteca.html', {'form': form, 'id_biblioteca': id_biblioteca})
    else:
        return render(request, 'error.html', {'message': 'Você não tem permissão para acessar esta página.'})

@login_required
def deletebiblioteca(request, id_biblioteca):
    if request.user.groups.filter(name='administrador').exists():
        biblioteca = get_object_or_404(Biblioteca, pk=id_biblioteca)
        biblioteca.delete()
        return HttpResponseRedirect('/biblioteca/')
    else:
        return render(request, 'error.html', {'message': 'Você não tem permissão para acessar esta página.'})

@login_required
def confirmDelete(request, id_biblioteca):
    if request.user.groups.filter(name='administrador').exists():
        biblioteca = get_object_or_404(Biblioteca, pk=id_biblioteca)
        return render(request, 'biblioteca/confirmdeletebiblioteca.html', {'biblioteca': biblioteca})
    else:
        return render(request, 'error.html', {'message': 'Você não tem permissão para acessar esta página.'})