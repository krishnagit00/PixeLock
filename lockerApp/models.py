from django.db import models
from django.utils import timezone
import random
import string
import datetime

class LockerUser(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class LockerFile(models.Model):
    # Image 0 shows files inside the locker
    user = models.ForeignKey(LockerUser, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='locker_files/%Y/%m/')
    filename = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # Add encryption fields here similar to TransferApp if locker files should also be encrypted at rest.

class VerificationToken(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = ''.join(random.choices(string.digits, k=6))
        super().save(*args, **kwargs)
        
    @property
    def is_valid(self):
        # Token valid for 15 minutes
        return self.created_at >= timezone.now() - datetime.timedelta(minutes=15)
