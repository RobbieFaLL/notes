from django.shortcuts import render

# Controller - also known as view

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
