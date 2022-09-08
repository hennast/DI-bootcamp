from django.urls import path

from .views import homepage, cardio



urlpatterns = [
    path('', homepage, name='home'),
    path('cardio', cardio, name='cardio'),
]