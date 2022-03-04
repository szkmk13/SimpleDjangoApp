from msilib.schema import ListView
from urllib import request
from django.db import DEFAULT_DB_ALIAS
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Person

class HomeView(ListView):
    model = Person
    krz=Person()
    krz.name="krzysiem"
    krz.msgs=109
    krz.zdj=10
    krz.reakcje=10
    krz.stopy=0
    krz.save
    template_name = "home.html"

class PersonDetailView(ListView):
    model = Person
    template_name = 'details.html'

class Krzysiem(ListView):
    model = Person
    template_name = "krzysiem.html"

class Szym(ListView):
    model = Person
    template_name = "szym.html"

class Karl(ListView):
    model = Person
    template_name = "karl.html"

class podstrona(DetailView):
    model = Person
    template_name= "person1.html"





# Create your views here.
