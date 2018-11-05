import uuid

from django.db import models

from apps.round.models import Rounds
from apps.player.models import Players


class Movements(models.Model):
    id = models.UUIDField(primary_key=True, null=False, blank=False, default=uuid.uuid4)
    round = models.ForeignKey(Rounds, on_delete=models.CASCADE)

    MOVEMENTS_CHOISES = (
        ("ROCK", "Rock"),
        ("PAPER", "Paper"),
        ("SCISSORS", "Scissors"),
    )

    player_1_movement = models.CharField(max_length=8, choices=MOVEMENTS_CHOISES)
    player_2_movement = models.CharField(max_length=8, choices=MOVEMENTS_CHOISES)
    created_at = models.DateTimeField(auto_now_add=True)

    winner = models.ForeignKey(Players, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "movements"
