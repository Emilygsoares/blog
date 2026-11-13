from django.urls import path
from . import views

urlpatterns = [
    # Rota para a página inicial 
    path('', views.home, name='home'),
    
    # Rota para a página de contatos
    path('contacts/', views.contacts, name='contacts'), 
]