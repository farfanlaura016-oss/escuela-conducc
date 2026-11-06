from django.urls import path
from .views import lista_clases

urlpatterns = [
    path('clases/', lista_clases, name='lista_clases'),
]