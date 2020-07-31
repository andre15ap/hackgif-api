from django.db import models

class Gif(models.Model):
    gif_url = models.CharField('Gif url', max_length=500)
    votes = models.IntegerField('Votos')


    def __str__(self):
        return '{} - {}'.format(str(self.id), self.gif_url)