from django.db import models

class Bikes(models.Model):
    class Meta:
        verbose_name_plural = "Bikes"

    images = models.ImageField(upload_to='media')
    title = models.CharField(max_length=255)
    description= models.TextField(max_length=10000)
    brand = models.CharField(max_length=255)
    modelname = models.CharField(max_length=255)
    specs = models.TextField(max_length=255)


class Wheel(models.Model):
    images = models.ImageField(upload_to='media')
    brand_name = models.CharField(max_length=30)
    model_name = models.CharField(max_length= 50)
    description = models.TextField(max_length=10000)
    internal_rim_width = models.CharField(max_length=10)
    external_rim_width = models.CharField(max_length=10)
    spokecount = models.IntegerField()
    spoke_materaial = models.CharField(max_length=20)
    rimdepth = models.CharField(max_length=10)
    axlesizeF = models.CharField(max_length=10)
    axlesizeR = models.CharField(max_length=10)
    weight_grams = models.IntegerField()
    brake_type = models.CharField(max_length=30)


class Tyre(models.Model):
    images = models.ImageField(upload_to='media')
    description = models.TextField(max_length=10000)
    width = models.CharField(max_length=10)
    colour = models.CharField(max_length=20)
    brand_name = models.CharField(max_length=20)
    model_name = models.CharField(max_length=30)
    weight_grams = models.IntegerField()
