from django import forms

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


# creating a form
class MonthForm(forms.Form):
    month_select = forms.ChoiceField(choices=MONTH_CHOICES)


class ScoreForm(forms.Form):
    file = forms.FileField()
