from django.urls import path

from api.v1.player.views import player_view

app_name = "player"

urlpatterns = [
    path('rank', player_view.get_players_rank_view),
]
