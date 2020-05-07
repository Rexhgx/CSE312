from django.db import models

from Account.models import User


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend_name = models.CharField(max_length=16)


class Message(models.Model):
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=16)
    receiver_name = models.CharField(max_length=16)
    content = models.CharField(max_length=150, blank=True, null=True)


class Room(models.Model):
    user_one = models.CharField(max_length=16)
    user_two = models.CharField(max_length=16)