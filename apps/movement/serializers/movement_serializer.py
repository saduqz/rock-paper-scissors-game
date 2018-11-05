from rest_framework import serializers

from apps.movement.models import Movements
from apps.player.serializers.player_serializer import PlayerSerializer


class MovementsSerializer(serializers.ModelSerializer):
    winner = PlayerSerializer(many=False, read_only=True)

    class Meta:
        model = Movements
        fields = ('id', 'round', 'player_1_movement', 'player_2_movement', 'winner', 'created_at')
        read_only_fields = ('id', 'created_at', 'winner')
