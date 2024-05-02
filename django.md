#django notes
my files:
- the outer mysite / root directory is a container for your project (namr doesn't matter)
- manage.py acmmand-line utility that lets you iteract with your djago project in various ways
- mysite/init.py an empty file that that tells python that this directory should be considered apython package
- mysite/settings.py settings/ config for django project
- mysite/urls.py the URL (uniformresource locator) declarations for this django project, a table of contents foryour site


#link for docs:
https://docs.djangoproject.com/en/5.0/intro/tutorial01/


#additinal:
 python manage.py startapp polls
That’ll create a directory polls, which is laid out like this:

polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
This directory structure will house the poll application.

Write your first view¶
Let’s write the first view. Open the file polls/views.py and put the following Python code in it:

polls/views.py¶
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
This is the simplest view possible in Django. To call the view, we need to map it to a URL - and for this we need a URLconf.

To create a URLconf in the polls directory, create a file called urls.py. Your app directory should now look like:

polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py