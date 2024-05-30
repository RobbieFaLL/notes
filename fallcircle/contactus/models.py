from django.db import models

class ContactUs(models.Model):
    class Meta:
        verbose_name_plural = "Contact us"
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, default= "Site Contact")
    email = models.EmailField()
    message = models.TextField(max_length=10000)

    def __str__(self):
        return self.subject
