from django.db import models

class Blog(models.Model):
    images = models.ImageField(upload_to='media')
    content = models.TextField(max_length=100000)
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    author = models.CharField(max_length=255)

    # 'dunder' method to output title instead of object referenceß
    def __str__(self):
        return self.title

