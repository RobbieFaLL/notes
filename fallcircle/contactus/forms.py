from django import forms 

class ContactUsform(forms.Form):
    name = forms.CharField(label="Name", max_length=150)
    email = forms.EmailField(label="your email")
    subject = forms.CharField(max_length = 255, label= "subject")
    message = forms.CharField(widget=forms.Textarea, label="message")
