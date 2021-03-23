from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.urls import reverse
from vendor.models import *
from users.models import *

# Create your models here.

class adoption(models.Model):
    #def upload_location(instance, filename):
    #    #filebase, extension = filename.split(".")
    #    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    #    return "%s/%s" %(instance.pet_id, filename)

    pet_id = models.AutoField(primary_key = True)
    pet_name = models.CharField(max_length = 30, null = True)
    pet_breed = models.CharField(max_length = 30)
    pet_type = models.CharField(max_length = 30)
    pet_gender = models.IntegerField(choices = ((0,'Male'),(1,'Female'),(2,'Dont wish to disclose')))
    pet_age = models.IntegerField()
    pet_color = models.CharField(max_length = 50, blank = True, null =  True)
    pet_count = models.IntegerField(default = 1)
    pet_images = models.ImageField(upload_to='pet_images', blank = True, null = True)
    pet_bio = models.TextField(max_length = 500)
    pet_point_of_contact = models.CharField(max_length = 500)
    #pet_point_of_contact = PhoneField(blank=True, help_text='Agency phone number')
    pet_email_id = models.EmailField()
    pet_adoption_location = models.CharField(max_length = 500)
    pet_location_longitude = models.CharField(max_length = 500)
    pet_location_latitude = models.CharField(max_length = 500)
    pet_adoption_status = models.CharField(choices = (('Available','Available'),('Adopted','Adopted')),
                                           default = 'Available', max_length = 10)
    #pet_adoption_centre_name = models.CharField(max_length = 50, null = True)
    pet_vendor = models.OneToOneField(vendor, on_delete=models.CASCADE)
    pet_adoption_centre_logo = models.ImageField(upload_to = 'adoption_centre_logo', blank = True, null = True)
    vendor_timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    vendor_update = models.DateTimeField(auto_now_add = False, auto_now = True)

    class Meta:
        db_table = "adoption"

    def __str__(self):
        return self.pet_name

    def get_absolute_url(self):
        #return reverse("adoption:detail", kwargs={"pk": self.pet_id})
        return reverse("adoption:detail", kwargs={"pk": self.pet_id})

    @property
    def pet_images_url(self):
        if self.pet_images:  #and hasattr(self.pet_images, 'url'):
            return self.pet_images.url
        return '#'



class adoption_request(models.Model): #main table 
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(user_login_details, on_delete=models.CASCADE) 
    question = models.ForeignKey(questionnaire, on_delete=models.CASCADE)
    pet = models.ForeignKey(adoption, on_delete=models.CASCADE)
    requested_at = models.DateTimeField(auto_now_add = True, auto_now = False)
    application_status =  models.IntegerField(choices = ((1,'Shortlisted'),(2,'Rejected'),(3,'Pending')),default=3)
    preferred_day = models.IntegerField(choices = ((1,'Weekday'),(2,'Weekend')),default=1)
    preferred_time = models.IntegerField(choices = ((1,'Morning'),(2,'Afternoon'),(3,'Evening')),default=2)
    #appointment = models.DateField(auto_now_add = False, auto_now = False)

    class Meta:
        db_table = "adoption_relation"

    #def __str__(self):
    #    return self.pet_id


#class adoption_items(models.Model):
#    pet_id = models.IntegerField()
#    adoptrelation = models.ForeignKey(adoption_relation, on_delete=models.CASCADE)
#    vendor_id = models.IntegerField()
#    application_status =  models.IntegerField(choices = ((1,'Selected'),(2,'Rejected'),(3,'Book an Appointment')))

#    class Meta:
#        db_table = "adoption_items"

#    def __str__(self):
#        return self.pet_id






