from django.urls import path
from .views import *

urlpatterns = [
    path('questions/', get_question, name='questions'),
    path('languages/', get_languages, name='languages'),
    path('advices/', get_carrierAdvice, name='advices'),
]