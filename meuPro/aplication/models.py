from django.db import models
#from django.contrib.auth.models import User

# Create your models here.


class Items(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    assunto = models.CharField(max_length=100)
    mensagem = models.TextField()

    class Meta:
        verbose_name_plural = 'Items'
        ordering = ('nome',)

    def __str__(self):
        return self.nome
