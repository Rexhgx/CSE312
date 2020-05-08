import random
import string

from django.db import models
from django.conf import settings


def post_photo_path(instance, filename):
    random_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    filename = random_number + filename
    return '/'.join(['share', instance.user.username, filename])


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_text = models.CharField(max_length=200)
    post_photo = models.FileField(upload_to=post_photo_path, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liker = models.CharField(max_length=16)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.CharField(max_length=16)
    comment_text = models.CharField(max_length=50)

