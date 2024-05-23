from django.urls import path
from .views import blog_index, blog_content


urlpatterns = [
    path('blog', blog_index, name='blog'),
    path('blog/<int:id>',blog_content, name='blog_content')

]