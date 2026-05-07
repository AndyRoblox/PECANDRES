from django.urls import path
from .views import game_view, ScoresAPIView

urlpatterns = [
    path('', game_view, name='game'),
    path('api/scores/', ScoresAPIView.as_view(), name='scores-api'),
    path('api/scores/', ScoresAPIView.as_view(), name='scores'),
    path('', game_view, name='juego'),
]