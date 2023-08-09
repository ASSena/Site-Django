from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.
LISTA_CATEGORIAS = (('ANALISE', 'Análise'), ('PROGRAMACAO', 'Programação'),('APRESENTACAO','Apresentação'), ('OUTROS', 'Outros'))
class Filme(models.Model):
    thumb = models.ImageField(upload_to='thumb_filmes/')
    titulo = models.CharField(max_length=100)
    visualizacoes = models.IntegerField(default=0)
    data_cracao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)

    def __str__(self):
        return self.titulo

# Criar episódios
class Episodio(models.Model):
    filme = models.ForeignKey('Filme',related_name='episodios', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.titulo

class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField('Filme')