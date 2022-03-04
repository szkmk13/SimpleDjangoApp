from unicodedata import name
from django import template

register = template.Library()

from ..models import Person


pkt_za_wiadomosc=0.25
pkt_za_zdj=1


dict={
    "krzysiem":[0,0],
    "szym":[0,0],
    "karl":[0,0],
    "absonic":[0,0]
    }
for man in Person.objects.all():
    if man.name in dict:
        dict[man.name][0]+=man.msgs
        dict[man.name][1]+=man.zdj


@register.filter
def suma_msg(a,imie):                         
    return dict[imie][0]

@register.filter
def suma_zdj(a,imie):
    return dict[imie][1]

@register.filter
def score(a,imie):
    return dict[imie][0] *pkt_za_wiadomosc + dict[imie][1] * pkt_za_zdj