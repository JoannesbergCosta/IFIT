from django.urls import path
from .views import IndexView

urlpatterns = [
    #path('endereço/', MinhaView.as_view(), name='nome_da_url'),
    path('inicio/', IndexView.as_view(), name='inicio'),
]