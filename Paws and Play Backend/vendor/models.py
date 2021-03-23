# Create your models here.

from __future__ import unicode_literals
from django.contrib.auth.models import User
#from django.conf import settings
from django.db import models
from PIL import Image
from phone_field import PhoneField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class vendor(models.Model):
    pet_adoption_centre_name = models.CharField(max_length = 50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    #username = models.CharField(max_length = 10) 
    #password = models.CharField(max_length = 15)
    #vendor_emailid = models.EmailField()
    pet_adoption_centre_logo = models.ImageField(upload_to = 'media/adoption_centre_logo', blank = True, null = True)
    vendor_contact = PhoneField(blank=True, help_text='Contact number')
    vendor_timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    vendor_update = models.DateTimeField(auto_now_add = False, auto_now = True)
    pet_adoption_location = models.CharField(max_length = 500)
    pet_location_longitude = models.CharField(max_length = 500)
    pet_location_latitude = models.CharField(max_length = 500)


    class Meta:
        db_table = "vendor"

    def __str__(self):
        return self.pet_adoption_centre_name

    def save(self):
        super().save()

        img = Image.open(self.pet_adoption_centre_logo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.pet_adoption_centre_logo.path)

    @property
    def pet_adoption_centre_logo_url(self):
        if self.pet_adoption_centre_logo and hasattr(self.pet_adoption_centre_logo, 'url'):
            return self.pet_adoption_centre_logo.url
        return '#'