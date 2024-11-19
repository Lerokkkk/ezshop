from django.contrib.auth import get_user_model
from django.contrib.auth.views import LogoutView, LoginView
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .models import User
from .serializers import UserRegisterSerializer, UserProfileSerializer


@extend_schema_view(
    post=extend_schema(
        summary="Регистрация нового пользователя",
        description="Создает нового пользователя в системе.",
        request=UserRegisterSerializer,
        responses={
            201: UserRegisterSerializer,
            400: {
                "type": "object",
                "properties": {
                    "detail": {"type": "string", "example": "Invalid data."},
                },
            },
        },
        tags=["Users"],
    )
)
class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


@extend_schema_view(
    get=extend_schema(
        summary="Просмотр профиля пользователя",
        description="Возвращает данные текущего авторизованного пользователя.",
        responses={
            200: UserProfileSerializer,
            401: {
                "type": "object",
                "properties": {
                    "detail": {"type": "string", "example": "Authentication credentials were not provided."},
                },
            },
        },
        tags=["Users"],
    )
)
class UserProfileView(RetrieveAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user
