from django import forms

from playground.models import Person

# iterable
MONTH_CHOICES = (
    ("1", "January"),
    ("2", "February"),
    ("3", "March"),
    ("4", "April"),
    ("5", "May"),
    ("6", "June"),
    ("7", "July"),
    ("8", "August"),
    ("9", "September"),
    ("10", "October"),
    ("11", "November"),
    ("12", "December"),
)


def get_person_choices(queryset):
    return [(user, user) for user in queryset]
# creating a form
class MonthForm(forms.Form):
    month_select = forms.ChoiceField(choices=MONTH_CHOICES)


class ScoreForm(forms.Form):
    file = forms.FileField()
    month_select = forms.ChoiceField(choices=MONTH_CHOICES)


class MessageForm(forms.Form):
    author = forms.ChoiceField(choices=get_person_choices(Person.objects.all()))
    message = forms.CharField(max_length=100)
    reactions = forms.IntegerField(min_value=0, required=False)


