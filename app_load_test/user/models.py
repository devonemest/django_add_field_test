from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(blank=True, max_length=255)
    age = models.IntegerField(blank=True, null=True)
    phone = models.CharField(blank=True, max_length=255)
    country = models.CharField(blank=True, max_length=255)
    city = models.CharField(blank=True, max_length=255)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.fullname

    class Meta:
        db_table = 'user'