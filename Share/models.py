from django.db import models
from Account.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_text = models.CharField(max_length=200)
    post_photo = models.ImageField(blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)