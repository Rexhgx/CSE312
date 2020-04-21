import uuid

from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=16, unique=True)
    user_password = models.CharField(max_length=16)
    user_token = models.UUIDField(default=uuid.uuid4)

