from django.urls import path, include

app_name = "v1"

urlpatterns = [
    path('rounds/', include('api.v1.round.urls', namespace='api-rounds')),
    path('movements/', include('api.v1.movement.urls', namespace='api-movements')),
    path('players/', include('api.v1.player.urls', namespace='api-players')),
]
