from django.shortcuts import render, redirect, reverse
from .forms import CriarContaForm, FormHomePage
from .models import Filme, Usuario
from django.views.generic import ListView, DetailView, TemplateView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomePage(FormView):
    template_name = 'homepage.html'
    form_class = FormHomePage
    def get(self, request, *args, **kwargs):
        # Se o usuario estiver autenticado
       if request.user.is_authenticated: # redireciona para a homefilmes
           return redirect('filme:homefilmes')
       else:
           return super().get(request, *args, **kwargs) # redireciona para a homepage

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuario = Usuario.objects.filter(email=email)
        if usuario:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')



class HomeFilmes(LoginRequiredMixin, ListView):
    template_name = 'homefilmes.html'
    model = Filme
    # retorna um object_list

class DetalhesFilme(LoginRequiredMixin, DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme

    def get(self, request, *args, **kwargs):
        # Encontra o filme, adiciona um ao número de visualizações e salva
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs) # redireciona para a página 

    def get_context_data(self, **kwargs):
        context = super(DetalhesFilme, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria= self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context

class PesquisaFilme(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Filme

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None

class EditarPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    template_name_suffix = "editarperfil.html"
    model = Usuario
    fields = ['first_name', 'last_name','email']

    def get_success_url(self):
        return reverse('filme:homefilmes')

class CriarConta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')
    # retorna um object

# def homepage(request):
#     return render(request, "homepage.html")

# url - view - html
# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)