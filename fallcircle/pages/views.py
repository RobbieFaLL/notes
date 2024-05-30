from django.shortcuts import render, get_object_or_404
from pages.models import Homepage, Aboutuspage
# Controller - also known as view

def index(request):
    title = Homepage.objects.all
    data = Homepage.objects.all
    return render(request, 'index.html')

def about(request):
    title = Aboutuspage.objects.all
    text = Aboutuspage.objects.all
    return render(request, 'about.html')
