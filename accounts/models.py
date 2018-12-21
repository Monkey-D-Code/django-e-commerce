from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user          = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number  = models.IntegerField(blank=False , unique=True)
    date          = models.DateField(auto_now=True)
    time          = models.TimeField(auto_now=True)
    
class Address(models.Model):

    address_type = (
        ('H' , 'Home'),
        ('N' , 'Neibour'),
        ('R' , 'Relative'),
        ('O' , 'Office'),
    )

    customer     = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name_plate   = models.CharField(blank=False , max_length=100)
    house_number = models.CharField(blank=False , max_length=50)
    locality     = models.CharField(blank=False, max_length=150)
    street       = models.CharField(blank=False , max_length=50)
    landmark     = models.CharField(blank=False , max_length=50)
    pin_code     = models.IntegerField(blank=False)
    type         = models.CharField(choices = address_type, max_length=50 , default='H')
    date         = models.DateField(auto_now=True)
    time         = models.TimeField(auto_now=True)



class Vendor(models.Model):

    user           = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.IntegerField(blank=False)
    address        = models.CharField(blank=False , max_length=150)
    date           = models.DateField(auto_now=True)
    time           = models.TimeField(auto_now=True)

class DeliveryPerson(models.Model):

    user           = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.IntegerField(blank=False)
    profile_photo  = models.URLField(blank=False, max_length=255)
    address        = models.CharField(blank=False , max_length=255)
    

