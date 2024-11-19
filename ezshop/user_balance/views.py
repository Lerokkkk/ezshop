from django.core.exceptions import ValidationError
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from user_balance.serializers import BalanceToUpSerializer, CheckoutSerializer
from user_balance.service import process_checkout


@extend_schema(
        request=BalanceToUpSerializer,
        responses={
            201: {
                "type": "object",
                "properties": {
                    "detail": {"type": "string", "example": "Баланс успешно пополнен. Текущий баланс: 1000"}
                }
            },
            400: {
                "type": "object",
                "properties": {
                    "detail": {"type": "string", "example": "Ошибки валидации"}
                }
            }
        },
        description="Пополняет баланс пользователя и возвращает его текущий баланс.",
        tags=["Balance"]
    )
class BalanceToUpView(CreateAPIView):
    serializer_class = BalanceToUpSerializer

    def perform_create(self, serializer):
        new_balance = serializer.save(user=self.request.user)
        self.new_balance = new_balance


    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        response.data = {
            'detail': f"Баланс успешно пополнен. Текущий баланс: {self.new_balance}"
        }
        return response


class CheckoutView(APIView):
    @extend_schema(
        request=CheckoutSerializer,
        responses={
            200: {
                "type": "object",
                "properties": {
                    "detail": {"type": "string", "example": "Баланс обновлен, корзина очищена"}
                }
            },
            400: {
                "type": "object",
                "properties": {
                    "detail": {"type": "string", "example": "Недостаточно средств на балансе"}
                }
            }
        },
        description="Обрабатывает платеж и обновляет баланс пользователя. Убирает все игры из корзины.",
        tags=["Checkout"]
    )
    def post(self, request, *args, **kwargs):
        serializer = CheckoutSerializer(data=request.data)
        if serializer.is_valid():
            total = serializer.validated_data['total']
            try:
                process_checkout(request.user, total)
                return Response({'detail': 'Баланс обновлен, корзина очищена'}, status=status.HTTP_200_OK)
            except ValidationError as e:
                return Response({"detail": e.message}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
