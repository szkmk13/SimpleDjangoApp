from django.urls import path
from .views import HomeView, PersonDetailView

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('details', views.PersonDetailView.as_view(), name='details'),

]


