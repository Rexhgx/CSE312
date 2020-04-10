import random
import string

from django.db import models
from Account.models import User


def post_photo_path(instance, filename):
    random_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    filename = random_number + filename
    return '/'.join(['share', instance.user.user_name, filename])


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_text = models.CharField(max_length=200)
    post_photo = models.ImageField(upload_to=post_photo_path, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liker = models.CharField(max_length=16)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.CharField(max_length=16)
    comment_text = models.CharField(max_length=50)

