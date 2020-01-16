from django.contrib.auth.models import AbstractUser
from django.db import models

SEX = (
    ('Man', 'Man'),
    ('Woman', 'Woman'),
    ('Unknown', 'Unknown')
)


# Create your models here.
class User(AbstractUser):
    birthday = models.DateTimeField()
    sex = models.CharField(choices=SEX, max_length=10)
