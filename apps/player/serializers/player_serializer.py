from rest_framework import serializers

from apps.player.models import Players


class PlayerSerializer(serializers.ModelSerializer):
    rounds_won = serializers.SerializerMethodField()

    def get_rounds_won(self, obj):
        # This can be done with a method like this, but for performance is better do the manual for.
        # return obj.rounds_set.filter(winner=obj).all().count()

        count = 0
        for roundObject in obj.rounds_set.all():
            print(count)
            if roundObject.winner_id == obj.id:
                print("x")
                count += 1
        return count

    class Meta:
        model = Players
        fields = ('id', 'username', 'created_at', 'rounds_won')
        read_only_fields = ('id', 'created_at', 'rounds_won')
