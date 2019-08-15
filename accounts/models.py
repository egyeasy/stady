from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=50, blank=True)
    school = models.CharField(max_length=30, blank=True)
    grade = models.IntegerField(null=True)
    