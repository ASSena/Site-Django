from .models import Filme

def filmes_novos(request):
    filme = Filme.objects.all().order_by('-data_cracao')[0:8]
    return {'filmes_novos': filme}

def filmes_emalta(request):
    filme = Filme.objects.all().order_by('-visualizacoes')[0:8]

    filme_destaque = filme and filme[0] or None
    return {'filmes_emalta': filme, 'filme_destaque': filme_destaque}