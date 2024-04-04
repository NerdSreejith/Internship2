from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class user_register(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='images/')
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name