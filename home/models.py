from django.db import models

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length=100)
    mode = models.CharField(max_length=10)



class Winnings(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=10)
    time = models.CharField(max_length=10)


class matchschedule(models.Model):
    time = models.CharField(max_length=5)
    soloplayers = models.CharField(max_length=10)
    squadlayers = models.CharField(max_length=10)
    duoteams = models.CharField(max_length=10)
    solowinprize = models.CharField(max_length=10)
    squadwinprize = models.CharField(max_length=10)
    duowinprize = models.CharField(max_length=10)
    soloentryfee = models.CharField(max_length=10)
    squadentryfee = models.CharField(max_length=10)
    duoentryfee = models.CharField(max_length=10)


class sliderimg(models.Model):
    img = models.ImageField(upload_to='pics')