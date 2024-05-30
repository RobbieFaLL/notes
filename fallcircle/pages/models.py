from django.db import models

# Create your models here.

class Homepage(models.Model):
    title = models.CharField(max_length = 255)
    data = models.TextField()

    def __str__(self):
        return self.title

class Aboutuspage(models.Model):
    title = models.CharField(max_length = 255)
    text = models.TextField()
    def __str__(self):
        return self.title