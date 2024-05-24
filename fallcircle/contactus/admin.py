from django.contrib import admin
from .models import ContactUs
# Register your models here.

class ContactusAdmin(admin.ModelAdmin):
    pass

admin.site.register(ContactUs, ContactusAdmin)

