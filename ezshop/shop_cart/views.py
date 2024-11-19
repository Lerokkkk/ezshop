from django.shortcuts import render, get_object_or_404
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status, mixins, viewsets
from rest_framework.response import Response
from games.models import Game
from games.serializers import GameSerializer
from .models import ShopCart
from .serializers import ShopCartSerializer, ShopCartListSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Список игр в корзине",
        description="Возвращает список игр, добавленных пользователем в корзину.",
        responses={
            200: ShopCartListSerializer,
        },
        tags=["ShopCart"]
    ),
    create=extend_schema(
        summary="Добавление игры в корзину",
        description="Добавляет игру в корзину текущего пользователя по game_id.",
        request=ShopCartSerializer,
        responses={
            201: GameSerializer,
            400: {
                "type": "object",
                "properties": {
                    "detail": {"type": "string", "example": "Игра уже в корзине"},
                },
            },
        },
        tags=["ShopCart"]
    ),
    destroy=extend_schema(
        summary="Удаление игры из корзины",
        description="Удаляет игру из корзины текущего пользователя по game_id.",
        responses={
            200: {
                "type": "object",
                "properties": {
                    "detail": {"type": "string", "example": "Игра удалена из корзины"},
                },
            },
            404: {
                "type": "object",
                "properties": {
                    "detail": {"type": "string", "example": "Not found."},
                },
            },
        },
        tags=["ShopCart"]
    )
)
class ShopCartViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = ShopCartSerializer

    def get_queryset(self):
        return ShopCart.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        game_id = kwargs.get('game_id')

        if ShopCart.objects.filter(user=request.user, game_id=game_id).exists():
            return Response({'detail': 'Игра уже в корзине'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data, context={'game_id': game_id, 'request': request})
        if serializer.is_valid():
            shop_cart = serializer.save()
            game = shop_cart.game
            game_serializer = GameSerializer(game)
            return Response(game_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        game_id = kwargs.get('game_id')
        shop_cart = get_object_or_404(ShopCart, user=request.user, game_id=game_id)

        shop_cart.delete()

        return Response({'detail': "Игра удалена из корзины"}, status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        games = Game.objects.filter(shop_cart__user=self.request.user)
        data = {
            'games': games
        }
        serializer = ShopCartListSerializer(data)

        return Response(serializer.data, status.HTTP_200_OK)
