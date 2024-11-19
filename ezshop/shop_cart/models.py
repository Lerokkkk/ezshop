from django.contrib.auth import get_user_model
from django.db import models
from games.models import Game

user = get_user_model()


class ShopCart(models.Model):

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        constraints = [
            models.UniqueConstraint(fields=['user', 'game'], name='unique_user_game_constraint')
        ]
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='shop_cart', verbose_name='корзина')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='shop_cart')

