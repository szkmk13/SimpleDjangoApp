from datetime import timedelta

import django_filters
from django.utils.timezone import now
from django_filters.filters import OrderingFilter
from django.utils.translation import gettext_lazy as _
from .models import Person, Score


class ProductFilter(django_filters.FilterSet):
    date_from__gt = django_filters.DateFilter(field_name='date_from', lookup_expr='gt')
    date_to__lt = django_filters.DateFilter(field_name='date_to', lookup_expr='lt')

    class Meta:
        model = Score
        fields = ['date_from', 'date_to']
