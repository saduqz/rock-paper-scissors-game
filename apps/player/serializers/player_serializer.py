from rest_framework import serializers

from apps.player.models import Players


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = ('id', 'username', 'created_at')
        read_only_fields = ('id', 'created_at',)
