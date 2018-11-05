import uuid
from django.db import models


class Players(models.Model):
    id = models.UUIDField(primary_key=True, null=False, blank=False, default=uuid.uuid4)
    username = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "players"
