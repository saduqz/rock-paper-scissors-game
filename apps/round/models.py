import uuid

from django.db import models

from apps.player.models import Players


class Rounds(models.Model):
    id = models.UUIDField(primary_key=True, null=False, blank=False, default=uuid.uuid4)
    player_1 = models.ForeignKey(Players, on_delete=models.CASCADE, related_name='player_1')
    player_2 = models.ForeignKey(Players, on_delete=models.CASCADE, related_name='player_2')
    winner = models.ForeignKey(Players, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "rounds"
