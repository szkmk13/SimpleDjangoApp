from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify # new

datawpisu = "teraz"

class Person(models.Model):                 # nazwa tego obiektu będize nazwą osoby w niej tylko liczby   
    name = models.CharField(max_length=30)
    slug = models.SlugField(null=False)
    def __str__ (self):
        return str(self.name)

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
        

class Score(models.Model):
    autor = models.ForeignKey(Person, on_delete=models.CASCADE)
   ## data = models.
    msgs = models.PositiveSmallIntegerField(default=0)
    zdj = models.PositiveSmallIntegerField(default=0)
    reakcje = models.PositiveSmallIntegerField(default=0)
    stopy = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return str(self.autor) # + str(self.data)
