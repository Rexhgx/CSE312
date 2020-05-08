from django.db import models
from django.conf import settings


class Friend(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    friend_name = models.CharField(max_length=16)


class Message(models.Model):
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=16)
    receiver_name = models.CharField(max_length=16)
    content = models.CharField(max_length=150, blank=True, null=True)


class Room(models.Model):
    user_one = models.CharField(max_length=16)
    user_two = models.CharField(max_length=16)