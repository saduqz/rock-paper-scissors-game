from rest_framework import serializers

from apps.round.models import Rounds

from apps.movement.serializers.movement_serializer import MovementsSerializer
from apps.player.serializers.player_serializer import PlayerSerializer


class RoundSerializer(serializers.ModelSerializer):
    movements_set = MovementsSerializer(many=True, read_only=True)
    winner = PlayerSerializer(many=False, read_only=True)
    player_1 = PlayerSerializer(many=False, read_only=True)
    player_2 = PlayerSerializer(many=False, read_only=True)

    class Meta:
        model = Rounds
        fields = ('id', 'player_1', 'player_2', 'winner', 'created_at', 'updated_at', 'movements_set')
        read_only_fields = ('id', 'created_at', 'updated_at')
