from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('', include('blog.urls')),
    path('',include('bikes.urls')),
    path('',include('contactus.urls'))

]