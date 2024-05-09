from django.contrib import admin
from . models import Bikes
from .models import Wheel
from .models import Tyre

class BikesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Bikes, BikesAdmin)

class WheelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Wheel, WheelAdmin)

class TyreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tyre, TyreAdmin)
