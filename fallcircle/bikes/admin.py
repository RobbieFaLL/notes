from django.contrib import admin
from . models import Bikes
from .models import Wheel
from .models import Tyre
from .models import Groupset
from .models import Chain

class BikesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Bikes, BikesAdmin)

class WheelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Wheel, WheelAdmin)

class TyreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tyre, TyreAdmin)

class GroupsetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Groupset, GroupsetAdmin)

class ChainAdmin(admin.ModelAdmin):
    pass

admin.site.register(Chain, ChainAdmin)






