import uuid
import random
import string

from django.db import models
from django.contrib.auth.models import AbstractUser


def user_photo_path(instance, filename):
    random_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    filename = random_number + filename
    return '/'.join(['profile', instance.username, filename])


class User(AbstractUser):
    photo = models.FileField(upload_to=user_photo_path, default='chat_and_share.png')
    token = models.UUIDField(default=uuid.uuid4)

