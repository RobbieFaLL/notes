from django.contrib import admin
from django.urls import path, include

import bikes


urlpatterns = [
    path('bikes', bikes, name='bikes'),

]