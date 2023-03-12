from django.db import models

# Create your models here.
class zomatoapitable(models.Model):
    hotel_name = models.CharField(max_length=20)
    area = models.CharField(max_length=15)
    number = models.BigIntegerField()
    special_menu = models.CharField(max_length=20)
