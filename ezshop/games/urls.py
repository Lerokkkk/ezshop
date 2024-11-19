from django.urls import path
from .views import GameListView, GameView

urlpatterns = [
    path("games/", GameListView.as_view(), name="game_list"),
    path("game/<int:pk>/", GameView.as_view(), name='game'),
]
