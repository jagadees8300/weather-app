from django.urls import path
from weatherapi.views import *

urlpatterns = [
    path('' , get_weather)
]