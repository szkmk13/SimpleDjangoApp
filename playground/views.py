from msilib.schema import ListView
from urllib import request
from django.db import DEFAULT_DB_ALIAS
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Person

class HomeView(ListView):
    template_name = "home.html"
    queryset = Person.objects.all()

class PersonDetailView(ListView):
    model = Person
    template_name = 'details.html'
