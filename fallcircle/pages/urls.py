from django.urls import path
from .views import about, index
from .views import bikes, index
from .views import contactus, index

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('bikes',bikes, name='bikes'),
    path('contactus',contactus, name='contactus')
]