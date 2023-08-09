# url - view - templates

from django.urls import path, reverse_lazy
from .views import HomePage, HomeFilmes,DetalhesFilme, PesquisaFilme, EditarPerfil, CriarConta
from django.contrib.auth import views as auth_viwes

app_name = 'filme'

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('filmes/', HomeFilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', DetalhesFilme.as_view(), name='detalhesfilme'),
    path('pesquisa/', PesquisaFilme.as_view(), name='pesquisafilme'),
    path('login/', auth_viwes.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_viwes.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>',EditarPerfil.as_view(), name='editarperfil'),
    path('cirarconta/',CriarConta.as_view(), name='criarconta' ),
    path('mudarsenha/', auth_viwes.PasswordChangeView.as_view(template_name='editarperfil.html', success_url= reverse_lazy('filme:homefilmes')), name='mudarsenha'),
]