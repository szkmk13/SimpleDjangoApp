from django.db import models
import json
from django.contrib.auth.models import User

datawpisu = "teraz"

class Person(models.Model):                 # nazwa tego obiektu będize nazwą osoby w niej tylko liczby   
    
   # a = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=30)
    msgs = models.PositiveSmallIntegerField(default=0)
    zdj = models.PositiveSmallIntegerField(default=0)
    reakcje = models.PositiveSmallIntegerField(default=0)
    stopy = models.PositiveSmallIntegerField(default=0)
    
    def __str__ (self):
        return str(self.name)


