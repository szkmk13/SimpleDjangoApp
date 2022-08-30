import json
from msilib.schema import ListView
from urllib import request
from django.db import DEFAULT_DB_ALIAS
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormView

from .filters import ProductFilter
from .forms import MonthForm, ScoreForm
from .models import Person, Score
from zipfile import ZipFile

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

    def get_filenames(self,path_to_zip):
        """ return list of filenames inside of the zip folder"""
        with ZipFile(path_to_zip, 'r') as zip:
            return zip.namelist()
    def get_trojmiejskie_file(self,filenames):
        base = 'messages/inbox/trojmiejskie'
        end = 'message_1.json'
        for name in filenames:
            if name.startswith(base) and name.endswith(end):
                return name

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        a = form.fields['file']
        file = request.FILES['file']
        if form.is_valid():
            #todo unzip file and get json data
            filenames = self.get_filenames(file)
            json_file = self.get_trojmiejskie_file(filenames)
            json_content = ZipFile(file).open(name=json_file, mode='r')
            c = json_content.read()

            my_json = c.decode('utf8').replace("'", '"')
            print(my_json)
            print('- ' * 20)




            return redirect(reverse('home'))
            # return self.form_valid(form)
        else:
            print("wrong")
            return self.form_invalid(form)



