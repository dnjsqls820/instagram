from django.db import models

class Account(models.Model):
    email = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    password = models.CharField(max_length=200)

# Create your models here.
