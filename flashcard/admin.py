from django.contrib import admin  # type: ignore
from .models import Categoria, Flashcard

admin.site.register(Categoria)
admin.site.register(Flashcard)
