from rest_framework import serializers

from apps.round.models import Rounds


class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rounds
        fields = ('id', 'player_1', 'player_2', 'winner', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
