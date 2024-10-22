# myproject/paginas/urls.py

from django.urls import path
from .views import IndexView, SobreView

urlpatterns = [
    path('', IndexView.as_view(), name='inicio'),
    path('sobre/', SobreView.as_view(), name='sobre'),     

]
