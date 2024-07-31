from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import userprofile
from django.http import HttpResponse

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            userprofile.objects.create(user=user)
            return redirect('/login/')
    else:
        # Se o método não for POST, cria um formulário vazio para ser exibido
        form = UserCreationForm()
    
    # Renderiza o template com o formulário
    return render(request, 'userprofile/signup.html', {'form': form})
