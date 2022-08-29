from django.db import models
import json
from django.contrib.auth.models import User
from django.db.models import CASCADE


class Person(models.Model):
    name = models.TextField(max_length=30)
    
    def __str__ (self):
        return str(self.name)

class Score(models.Model):
    owner = models.ForeignKey(Person, on_delete=CASCADE)
    messages = models.PositiveSmallIntegerField(default=0)
    photos = models.PositiveSmallIntegerField(default=0)
    reactions = models.PositiveSmallIntegerField(default=0)
    feet = models.PositiveSmallIntegerField(default=0)
