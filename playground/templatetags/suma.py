from unicodedata import name
from django import template

register = template.Library()

from ..models import Person

#Person.objects.create(name="krzysiem",msgs=10,zdj=10,reakcje=10,stopy=0)


trojmiejskie_dict={         #tutaj zrobić cały dict z listami?
        "krzysiem":0,
        "szym":0,
        "karl":0
    }

@register.filter
def suma_msg(a,imie):                               #a tutaj tylko zwracać poszczególne rzeczy ?
    
    dict=trojmiejskie_dict.copy()
    for man in Person.objects.all():
            if man.name in dict:
                dict[man.name]+=man.msgs
    return dict[imie]

@register.filter
def suma_zdj(a,imie):
    dict=trojmiejskie_dict.copy()                   #a tutaj tylko zwracać poszczególne rzeczy ?
    for man in Person.objects.all():
            if man.name in dict:
                dict[man.name]+=man.zdj
    return dict[imie]

@register.filter
def score(a,imie):
    dict={"krzysiem":[0,0]}
    for man in Person.objects.all():
            if man.name in dict:
                dict[man.name][0]+=man.msgs
                dict[man.name][1]+=man.zdj
    return dict[imie][0] * dict[imie][1]