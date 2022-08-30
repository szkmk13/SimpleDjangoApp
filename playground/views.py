from msilib.schema import ListView
from urllib import request
from django.db import DEFAULT_DB_ALIAS
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, FormView

from .filters import ProductFilter
from .forms import MonthForm, ScoreForm
from .models import Person, Score


class HomeView(ListView):
    template_name = "home.html"
    context_object_name = "pepole"
    filterset_class = ProductFilter
    queryset = Person.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = MonthForm
        context['filter'] = ProductFilter
        return context


class PersonDetailView(ListView):
    model = Person
    template_name = 'details.html'

class AddScoreView(FormView):
    template_name = "add_score.html"
    model = Score
    form_class = ScoreForm


