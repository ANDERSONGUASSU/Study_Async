from django.urls import path  # type: ignore
from . import views

urlpatterns = [
    path('novo_flashcard/', views.novo_flashcard, name='novo_flashcard'),
]
