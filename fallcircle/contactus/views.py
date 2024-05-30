from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactUs
from .forms import ContactUsform
# Create your views here.



def contactus(request):
   
    if request.method == 'POST':
        form = ContactUsform(request.POST)
        '''
        post request 
        case 1 validation error = set form to form with problems
        case 2 form is valid = process form 
        '''
        if form.is_valid():
            #get values from form
            name= form.cleaned_data["name"]
            subject= form.cleaned_data["subject"]
            email= form.cleaned_data["email"]
            message= form.cleaned_data["message"]
            #create and save contact
            contact = ContactUs(
                name = name, 
                subject = subject, 
                email = email,
                message = message)
            contact.save()
            messages.success(request, " thanks for contacting")
            return redirect("/")
        
        
    else:
        '''
        get request = set form to empty form
         
        '''
        form = ContactUsform() #
    context = {'form' : form}
    return render(request, "contactus.html", context)