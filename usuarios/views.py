from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def cadastro(request):

    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')

    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        

        if len(nome.strip())==0 or len(email.strip())==0 or len(senha.strip())==0 or len(confirmar_senha.strip())==0 :
            messages.add_message(request, constants.ERROR, 'Por favor preencha todos os campos.')
            return render(request ,'cadastro.html')
        elif senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Digite senhas correspondentes.')
            return render(request ,'cadastro.html')
        try:
            user = User.objects.create_user(
                username= nome,
                email= email,
                password=senha
            )
            #mensagem de sucesso
            messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso.')
            return render(request , "cadastro.html")
        except:
            #mensagem de erro
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema, Tente novamente dentro de uns minutos.')
            return render(request , "cadastro.html")
           


def logar(request):

    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')

    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
#authenticate- essa funcao retorna none caso nao exista  usuario como as credencias e nome do usuario caso exista.
        user = authenticate(username=nome ,password=senha)
        if user is not None:
            login(request, user)
            return render (request,'/divulgar/novo_pet')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return render(request, 'login.html')

def sair(request):
    logout(request)
    return redirect('/auth/login')