from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.start_game, name = 'start-game'),
    path('view/', views.game_view, name = 'game-view'),
    path('move/', views.move_piece, name = 'piece-move')    
]
