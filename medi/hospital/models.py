import email
from email.mime import image
from email.policy import default
from django.db import models

# Create your models here.


class hos_list(models.Model):
    hos_name = models.CharField(max_length=50)
    location =models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    date = models.DateField()
    image = models.ImageField(upload_to="hospital/images")
    services = models.CharField(max_length=1000,default="")
    contact = models.IntegerField(default=0)
    hos_beds = models.IntegerField(default=0)

    def __str__(self):
        return self.hos_name


class reviews(models.Model):
    reviewm = models.CharField(max_length=300)