from django.db import models

# Create your models here.
from authenicate.models import User


class Note(models.Model):
    text = models.CharField(max_length=1000)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', ]
