from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings

from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    credits = models.IntegerField(default=20)  # Every user gets 20 free credits daily

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    credits = models.IntegerField(default=5)  # Daily free scans
    last_updated = models.DateField(auto_now=True)

