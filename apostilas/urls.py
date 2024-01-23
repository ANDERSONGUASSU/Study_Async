from django.urls import path  # type: ignore
from . import views

app_name = 'apostilas'

urlpatterns = [
    path(
        'adicionar_apostilas/',
        views.adicionar_apostilas,
        name='adicionar_apostilas',
    ),
    path('apostila/<int:id>', views.apostila, name='apostila'),
]
