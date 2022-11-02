from django.db import models
from django.contrib.auth.models import AbstractUser


class Accounts(AbstractUser):
    group_number = models.IntegerField(blank=True, null=True)
