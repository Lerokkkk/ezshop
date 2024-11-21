from django.shortcuts import get_object_or_404
from rest_framework import serializers

from games.models import Game
from games.serializers import GameSerializer
from shop_cart.models import ShopCart
from users.serializers import UserProfileSerializer


class ShopCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopCart
        fields = ()

    def create(self, validated_data):
        user = self.context['request'].user
        game_id = self.context['game_id']

        game = get_object_or_404(Game, pk=game_id)

        shop_cart = ShopCart.objects.create(user=user, game=game)
        return shop_cart


# class ShopCartListSerializer(serializers.Serializer):
#     games = GameSerializer(many=True)
#     total_price = serializers.SerializerMethodField()
#
#     def get_total_price(self, obj):
#         print(obj)
#         return sum(game.price for game in obj['games'])

class ShopCartListSerializer(serializers.Serializer):
    games = serializers.SerializerMethodField()  # Используем метод для сериализации игр
    total_price = serializers.SerializerMethodField()

    def get_games(self, obj):
        # Передаём контекст дочернему сериализатору
        return GameSerializer(obj['games'], many=True, context=self.context).data

    def get_total_price(self, obj):
        return sum(game.price for game in obj['games'])