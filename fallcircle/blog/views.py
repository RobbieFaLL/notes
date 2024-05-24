from django.shortcuts import render, get_object_or_404
from blog.models import Blog

# Create your views here.

def blog_index(request):
    #get all blogs from daabase via ORM
    blog_posts = Blog.objects.all().order_by('-date')
    #pass blog posts to context
    context = {'posts':blog_posts}
    #pass request,template context to render
    return render(request, 'blog.html', context)

def blog_content(request, id):
    #getting blog content from database if it exists
    blog = get_object_or_404(Blog, pk=id)
    #pass blog to context
    context = {'post':blog}
    #pass request,template context to render
    return render(request, 'blogdetail.html', context)