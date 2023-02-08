from http import client
from django.db import models
from datetime import datetime, date

# Create your models here.
class jetski(models.Model):
    clientname = models.CharField(max_length=20)
    contact = models.CharField(max_length = 100)
    quantity = models.CharField(max_length = 50)




class ponton(models.Model):
    clientname = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    quantity = models.CharField(max_length = 100)



class yacht(models.Model):
    clientname = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    quantity = models.CharField(max_length=20)
    