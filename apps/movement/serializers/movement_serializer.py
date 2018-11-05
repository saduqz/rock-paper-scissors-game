from rest_framework import serializers

from apps.movement.models import Movements


class MovementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movements
        fields = ('id', 'round', 'player_1_movement', 'player_2_movement', 'winner')
        read_only_fields = ('id', 'created_at', 'winner')
