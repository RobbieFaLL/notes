from django.contrib import admin
from .models import Homepage
from .models import AboutUs

class PagesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Homepage, PagesAdmin)
admin.site.register(AboutUs, PagesAdmin)


# Register your models here.
