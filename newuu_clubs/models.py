from django.db import models


class Clubs(models.Model):
    club_name = models.CharField(max_length=100)
    club_definition = models.TextField(max_length=300)
    club_time = models.CharField(max_length=100)
    club_topic = models.TextField(max_length=500)
    active_students = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
