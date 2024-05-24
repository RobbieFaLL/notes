from django.urls import path
from .views import contactus

urlpatterns = [
    path('contactus', contactus, name='contactus'),

]