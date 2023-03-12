from django.db import models

# Create your models here.
class womenmodel(models.Model):
    img = models.ImageField(upload_to="static/media/", default=None)
    name= models.CharField(max_length=15)
    age= models.IntegerField()
    city= models.CharField(max_length=15)
    salary = models.IntegerField()