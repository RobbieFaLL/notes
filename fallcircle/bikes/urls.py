from django.urls import path
from .views import bikes, bikes_content

urlpatterns = [
    path('bikes', bikes, name='bikes'),
    path('bikes/<int:id>',bikes_content, name='bikes_content'),
]