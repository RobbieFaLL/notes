from django.shortcuts import render

# Create your views here.

def bikes(request):
    return render(request, 'bikes.html')