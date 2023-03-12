from django.db import models

# Create your models here.
class logintable(models.Model):
    contact=models.CharField(max_length=10, unique=True)
    session_id = models.CharField(max_length=100)
