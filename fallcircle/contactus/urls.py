
from django.urls import path

from contactus.views import contactus


urlpatterns = [
    path('contactus', contactus, name='contactus'),

]