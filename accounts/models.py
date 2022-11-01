from django.db import models
from django.contrib.auth.models import AbstractUser


class Accounts(AbstractUser):
    fullname = models.CharField(blank=False)
    group_number = models.IntegerField(blank=False)
