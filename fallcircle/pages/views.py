from django.shortcuts import render, get_object_or_404
from pages.models import Homepage, AboutUs
# Controller - also known as view

def index(request):
    page = get_object_or_404(Homepage)
    context = {
        'page': page
    }
    return render(request, 'index.html', context)


def about(request):
    html = AboutUs.objects.first()
    return render(request, 'about.html', {'content': html})
