from django.shortcuts import render, redirect  # type: ignore
from .models import Categoria, Flashcard


def novo_flashcard(request):
    if not request.user.is_authenticated:
        return redirect('login.html')

    if request.method == 'GET':
        categorias = Categoria.objects.all()
        dificuldades = Flashcard.DIFICULDADE_CHOICES

        return render(
            request,
            'novo_flashcard.html',
            {
                'categorias': categorias,
                'dificuldades': dificuldades,
            },
        )
