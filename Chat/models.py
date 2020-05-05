from django.db import models

from Account.models import User


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend_name = models.CharField(max_length=16)
