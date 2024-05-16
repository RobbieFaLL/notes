from django.db import models

ROTOR_CHOICES = [
    ("140", "140mm"),
    ("160", "160mm"),
    ("160/140", "160mm / 140mm"),
    ("180", "180mm"),
    ("200", "200mm"),
]
CRANKSET_CHOICES = [
    ("50/34", "compact"),
    ("52/36", "semi-compact"),
    ("non-standard", "other"),
]

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

    def __str__(self):
        return self.model_name
    
class Tyre(models.Model):
    images = models.ImageField(upload_to='media')
    description = models.TextField(max_length=10000)
    width = models.CharField(max_length=10)
    colour = models.CharField(max_length=20)
    brand_name = models.CharField(max_length=20)
    model_name = models.CharField(max_length=30)
    weight_grams = models.IntegerField()
    

    def __str__(self):
        return self.model_name

class Chain(models.Model):
    images = models.ImageField(upload_to='media')
    model_name = models.CharField(max_length=255)
    links_count = models.BigIntegerField()
    brand_name = models.CharField(max_length=255)
    colour = models.CharField(max_length=255)

    def __str__(self):
        return self.model_name
    


class Groupset(models.Model):
    images = models.ImageField(upload_to='media')
    model_name = models.CharField(max_length=255)
    rotor_size = models.CharField(max_length= 255 , choices=ROTOR_CHOICES)
    Crankset = models.CharField(max_length=255 , choices=CRANKSET_CHOICES, default= "not set")
    other = models.CharField(max_length=255, default= "N/A")
    Chain = models.ForeignKey(Chain, on_delete=models.SET_NULL,null=True)

    
    def __str__(self):
        return self.model_name


class Bikes(models.Model):
    class Meta:
        verbose_name_plural = "Bikes"

    images = models.ImageField(upload_to='media')
    title = models.CharField(max_length=255)
    description= models.TextField(max_length=10000)
    brand = models.CharField(max_length=255)
    modelname = models.CharField(max_length=255)
    specs = models.TextField(max_length=255)
    wheels = models.ForeignKey(Wheel, on_delete=models.SET_NULL,null=True)
    Tyre = models.ForeignKey(Tyre, on_delete=models.SET_NULL,null=True)
    Groupset = models.ForeignKey(Groupset, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title



