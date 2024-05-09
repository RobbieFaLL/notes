from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField(max_length=10000)

    def __str__(self):
        return self.title
