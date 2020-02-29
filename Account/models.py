from django.db import models


class User(models.Model):
    u_name = models.CharField(max_length=16, unique=True, db_index=True)
    u_password = models.CharField(max_length=16, db_index=True)
