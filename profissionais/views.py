from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as login_django
from django.contrib.auth import logout
from django.shortcuts import redirect
from profissionais.forms import ProfissionalForm # type: ignore
from .models import Profissional

#lista profissionais cadastrados
def profissionais(request):

   # usuario = Usuario.objects.get(username=request.user)
   # isAdmin = usuario.groups.get(name='administrador')
   # if isAdmin:
        #faça aqui
   # else:
        #faça aqui

    profissionais = Profissional.objects.all()
  
    return render(request, 'profissionais.html', {'profissionais': profissionais})
    #return render(request, 'profissionais.html')
  
# cria profissionais 
def createprofissionais(request):
    if request.method == 'POST':
        form = ProfissionalForm(request.POST)
        if form.is_valid():
            form.save()
           # return redirect('createprofissionais')
            return HttpResponseRedirect("/profissionais/createprofissionais")
    else:
        form = ProfissionalForm()
    
    return render(request, 'createprofissionais.html', {'form': form})
