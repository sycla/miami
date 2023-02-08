from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    totalmatch = models.CharField(max_length=5)
    totalwinmoney = models.CharField(max_length=10)
    roomid = models.CharField(max_length=50)
    roompassword = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super(Profile,self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



# class matchschedule(models.Model):
#     time = models.CharField(max_length=5)
#     soloplayers = models.CharField(max_length=10)
#     squadlayers = models.CharField(max_length=10)
#     duoteams = models.CharField(max_length=10)
#     solowinprize = models.CharField(max_length=10)
#     squadwinprize = models.CharField(max_length=10)
#     duowinprize = models.CharField(max_length=10)
#     soloentryfee = models.CharField(max_length=10)
#     squadentryfee = models.CharField(max_length=10)
#     duoentryfee = models.CharField(max_length=10)