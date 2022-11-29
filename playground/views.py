import json
from msilib.schema import ListView
from urllib import request
from django.db import DEFAULT_DB_ALIAS
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, FormView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from .filters import ProductFilter
from .forms import MonthForm, ScoreForm, MessageForm
from .models import Person, Score, ChatMessage, Word
from zipfile import ZipFile


class MessagesView(ListView):
    template_name = "messages.html"
    context_object_name = "messages"
    queryset = ChatMessage.objects.all()


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


class AddMessageView(FormView):
    template_name = "add_message.html"
    form_class = MessageForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid:
            sender = Person.objects.filter(name__exact=form.data['author']).first()
            message = form.data['message']
            ChatMessage.objects.create(sender=sender, message=message, send_at=timezone.now())
            words = message.split(" ")
            for word in words:
                word_obj = Word.objects.filter(sender=sender).filter(message=word).first()
                if word_obj:
                    word_obj.count += 1
                    word_obj.save()
                else:
                    Word.objects.create(sender=sender, message=word, count=1)
            return redirect(reverse('home'))
        else:
            return self.form_invalid(form)


class AddScoreView(FormView):
    template_name = "add_score.html"
    form_class = ScoreForm

    def get_filenames(self, path_to_zip):
        """ return list of filenames inside the zip folder"""
        with ZipFile(path_to_zip, 'r') as zipped:
            return zipped.namelist()

    @staticmethod
    def get_trojmiejskie_file(filenames):

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
            # todo unzip file and get json data
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
