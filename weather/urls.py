from django.urls import path
from .views import *

urlpatterns = [
    path('',get_weather,name='get_weather'),
]
