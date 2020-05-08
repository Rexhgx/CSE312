import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    token = models.UUIDField(default=uuid.uuid4)

