from django.shortcuts import render, get_object_or_404
from pages.models import Homepage, Aboutuspage
# Controller - also known as view

def index(request):
    page = get_object_or_404(Homepage)
    context = {
        'page': page
    }
    return render(request, 'index.html', context)

def about(request):
    page = get_object_or_404(Aboutuspage)
    context = {
        'page': page
    }

    return render(request, 'about.html', context)
