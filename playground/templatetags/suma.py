from unicodedata import name
from django import template

register = template.Library()

from ..models import  Person, Score


pkt_za_wiadomosc=0.25
pkt_za_zdj=1


dict={
    "Kicky":[0,0,0,0,0,0],
    "Szymon":[0,0,0,0,0,0],
    "Larox":[0,0,0,0,0,0],
    "Kuba":[0,0,0,0,0,0],
    "Daniel":[0,0,0,0,0,0],
    "Mati":[0,0,0,0,0,0],
    "Duży":[0,0,0,0,0,0],
    "Karol Pępiak":[0,0,0,0,0,0],
    "Daleki":[0,0,0,0,0,0],
    "Olek":[0,0,0,0,0,0],
    "Absonic":[0,0,0,0,0,0],
    }
"""                         """
for man in Score.objects.all():         # man.autor.name -> str || man.autor -> class object
    dict[man.autor.name][0]+=man.msgs 
    dict[man.autor.name][1]+=man.zdj
    dict[man.autor.name][2]+=man.reakcje
    dict[man.autor.name][3]+=man.stopy

@register.filter
def suma_msg(a,imie):                       
    return dict[imie][0]

@register.filter
def suma_zdj(a,imie):
    return dict[imie][1]

@register.filter
def suma_reakcje(a,imie):
    return dict[imie][2]

@register.filter
def suma_stopy(a,imie):
    return dict[imie][3]


@register.filter
def score(a,imie):
    return dict[imie][0] *pkt_za_wiadomosc + dict[imie][1] * pkt_za_zdj