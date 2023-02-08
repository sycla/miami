from django.db import models

# Create your models here.

class matchregistration(models.Model):
    characterid = models.CharField(max_length=20)
    transid = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 50)




class duomatchregistration(models.Model):
    duocharacterid1 = models.CharField(max_length=20)
    duocharacterid2 = models.CharField(max_length=20)
    duotransactionid = models.CharField(max_length = 100)
    duophone = models.CharField(max_length = 50)



class squadmatchregistration(models.Model):
    squadcharacterid1 = models.CharField(max_length=20)
    squadcharacterid2 = models.CharField(max_length=20)
    squadcharacterid3 = models.CharField(max_length=20)
    squadcharacterid4 = models.CharField(max_length=20)
    squadtransactionid = models.CharField(max_length = 100)
    squadphone = models.CharField(max_length = 50)