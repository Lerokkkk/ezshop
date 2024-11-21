from django.db import models


# Create your models here.
class Game(models.Model):
    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    description = models.CharField(max_length=500, verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    photo = models.ImageField(upload_to='games_photo', null=True, default=None, verbose_name='Фото')

    def __str__(self):
        return self.title
