from django.db import models
<<<<<<< HEAD
from django.conf import settings  # Import settings to access AUTH_USER_MODEL

class Document(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
=======

# Create your models here.
>>>>>>> fc540e5 (Initial commit - Django setup for CrediScan)
