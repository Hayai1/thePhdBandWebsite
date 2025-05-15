
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', view=views.home, name='home'),
    path('about/', view=views.about, name='about'),
    path('music/', view=views.music, name='music'),
    path('tour/', view=views.tour, name='tour'),
    path('contact/', view=views.contact, name='contact'),

    ]
