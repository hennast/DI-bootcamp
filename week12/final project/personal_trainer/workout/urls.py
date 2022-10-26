from django.urls import path

from .views import homepage, cardio, strength, speed, endurance


app_name = 'workout'
urlpatterns = [
    path('', homepage, name='home'),
    path('cardio', cardio, name="cardio"),
    path('strength', strength, name="strength"),
    path('speed', speed, name="speed"),
    path('endurance', endurance, name="endurance"),
]