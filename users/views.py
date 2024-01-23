from django.shortcuts import render, redirect  # type: ignore
from django.contrib.messages import constants  # type: ignore
from django.contrib import messages, auth  # type: ignore
from django.contrib.auth.models import User  # type: ignore


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        if not senha == confirmar_senha:
            messages.add_message(
                request,
                constants.ERROR,
                'Ops! Senhas não coincidem. Verifique!.',
            )

            return redirect('cadastro')
        user = User.objects.filter(username=username)
        if user.exists():
            messages.add_message(
                request, constants.ERROR, 'Usuário já existe.'
            )
            return redirect('cadastro')
        try:
            User.objects.create_user(
                username=username,
                password=senha,
            )
            return redirect('login')
        except User.DoesNotExist:
            return redirect('cadastro')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=username, password=senha)
        if user:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Logado')
            return redirect('flashcard:novo_flashcard')
        else:
            messages.add_message(
                request, constants.ERROR, 'Username ou senha inválidos'
            )
            return redirect('login')


def logout(request):
    auth.logout(request)
    return redirect('login')
