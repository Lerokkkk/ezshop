from django.urls import path, include
from .views import RegisterUserView, UserProfileView

urlpatterns = [
    path('registration/', RegisterUserView.as_view()),

    path('profile/', UserProfileView.as_view(), name='profile'),
]
