from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Homepage(models.Model):
    title = models.CharField(max_length = 255)
    data = RichTextField()

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=200, default="About Us")
    welcome_message = RichTextField()
    who_we_are = RichTextField()
    what_we_do = RichTextField()
    why_choose_us = RichTextField()

    def __str__(self):
        return self.title
