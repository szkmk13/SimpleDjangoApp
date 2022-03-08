from msilib.schema import ListView
from typing import List
from urllib import request
from django.db import DEFAULT_DB_ALIAS
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Person, Score

class HomeView(ListView):
    model = Person

    template_name = "home.html"

class PersonDetailView(ListView):
    template_name = 'details.html'
  
    def get_queryset(self):
        self.name = get_object_or_404(Person, id=self.kwargs['id'])
        person_name = self.name
        return Score.objects.filter(autor=self.name)
    
