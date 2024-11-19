from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import AllowAny

from .models import Game
from .serializers import GameSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView


@extend_schema_view(
    get=extend_schema(
        summary="Получение списка игр",
        description="Возвращает список всех игр в базе данных.",
        responses={
            200: GameSerializer(many=True),
        },
        tags=["Games"],
    )
)
class GameListView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [AllowAny]


@extend_schema_view(
    get=extend_schema(
        summary="Получение одной игры",
        description="Возвращает информацию об игре по ID.",
        responses={
            200: GameSerializer,
            404: {
                "type": "object",
                "properties": {
                    "detail": {"type": "string", "example": "Not found."},
                },
            },
        },
        tags=["Games"],
    )
)
class GameView(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [AllowAny]
