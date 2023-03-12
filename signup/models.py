from django.db import models
from django.contrib.auth.hashers import make_password




# Create your models here.
class signupmodel(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    dob = models.DateField(default=None)
    menu = [('Male', 'male'), ('Female', 'female'), ('Others', 'others')]
    gender = models.CharField(max_length=7, choices=menu, default='Male')
    email=models.EmailField(max_length=50, unique=True)
    contact=models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(signupmodel, self).save(*args, **kwargs)



