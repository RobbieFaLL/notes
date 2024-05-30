from django.shortcuts import render
from .forms import ContactUs
# Create your views here.



def contactus(request):
    form = ContactUs()
    context = {'form' : form}
    return render(request, 'contactus.html', context)
