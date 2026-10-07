from django.db import models

class Socialnetwork(models.Model):
    name = models.CharField('Nome', max_length=50)
    content_type = models.TextField('Tpo do conteúdo', max_length=100)
    url = models.CharField('Link da Rede Social', max_length=200)

    class Meta:
        verbose_name = 'Rede Social'
        verbose_name_plural = 'Redes Sociais'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'