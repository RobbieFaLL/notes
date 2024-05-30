from django.contrib import admin
from .models import Homepage
from .models import Aboutuspage

class PagesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Homepage, PagesAdmin)
admin.site.register(Aboutuspage, PagesAdmin)


# Register your models here.
