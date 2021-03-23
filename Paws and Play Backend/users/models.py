# Create your models here.

from __future__ import unicode_literals
from django.db import models
from phone_field import PhoneField
from django.conf import settings

#from webapp.models import adoption

class user_login_details(models.Model):
    fb_token = models.CharField(max_length = 1000)
    user_first_name = models.CharField(max_length = 100)
    user_last_name = models.CharField(max_length = 100)
    user_profile_pic = models.TextField( blank = True, null = True)
    user_email_id  = models.EmailField()
    #pet_id = models.ManyToManyRel(adoption)
    #application_status =  models.IntegerField(choices = ((1,'Selected'),(2,'Rejected'),(3,'Book an Appointment')))

    class Meta:
        db_table = "user_login_details"

    def __str__(self):
        return self.user_first_name


####################### pet_owner ##########################################

class owner(models.Model):
    user = models.OneToOneField(user_login_details,on_delete=models.CASCADE)
    name = models.CharField(max_length = 20)
    photo = models.ImageField(upload_to='owner', blank = True, null = True)
    sex = models.CharField(max_length = 1, choices = (('M','Male'),('F','Female'),('W','Dont wish to disclose')))
    bio = models.TextField(max_length = 500)
    dob = models.DateField(max_length=8)                #import birthday
    longitude = models.CharField(max_length = 500)
    latitude = models.CharField(max_length = 500)
    home_address = models.CharField(max_length = 500)
    emergency_address = models.CharField(max_length = 500)
    emergency_contact = PhoneField(blank=True, help_text='Emergency Contact number')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    no_of_pets = models.IntegerField(default = 0)

    class Meta:
        db_table = "owner"

    def __str__(self):
        return self.name

####################### questionnaire ##########################################

class questionnaire(models.Model):
    user_id = models.ForeignKey(user_login_details, on_delete = models.CASCADE)
    ##pet_id = models.ForeignKey(adoption, on_delete = models.CASCADE)
    user_timestamp = models.DateTimeField(auto_now_add = True)
    #user_fullname = models.CharField(max_length = 100)
    user_age = models.IntegerField(null = True,blank=True)
    ##user_emailid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    #user_emailid = models.EmailField()
    user_contact_number = PhoneField(blank=True, help_text='Contact number') 
    #user_share_contact_number = models.IntegerField(choices = ((0,'Yes'),(1,'No')),default = 0)
    user_existing_pet_details =  models.IntegerField(choices =((1,'Yes, I have had pets in the past'),
                                                               (2,'No, I have no relation to them'),
                                                               (3,'I donot remember'),
                                                               (4,'I am not sure if i could be counted as a pet to my parents')))
    user_home_size = models.IntegerField(choices = ((1,'1 BHK'),(2,'<2 BHK'), (3,'Villa'),(4,'Cubical'),(5,'Mini home')))
    user_flatmates = models.IntegerField(choices=((1,'Friends'),(2,'Family'),(3,'Friends and Family'),
                                                  (4,'Friends who could turn into family'),
                                                  (5,'I do not like living with anyone')))
    user_job_timings = models.IntegerField(choices=((1,'9AM- 5PM( Regular government job)'), (2,'IT employee'), 
                                                     (3,'Startup employee(Not sure if i go home regularly)'), (4,'Freelancer(I am the king)'),
                                                     (5,'I donot need to work because I am still a student/king of my empire')))
    user_income = models.IntegerField(choices=((1,'5000-25000(Before EMIs)'),(2,'20000-80000(Before EMIs)'),(3,'No steady income'),(4,'I am rich'),
                                               (5,'Write your own answer')))
    user_godfather_details = models.TextField()
    user_parenting_style = models.IntegerField(choices=((1,'Tough parent'),(2,'Soft parent'),(3,' I am not sure parent'),
                                                        (4,'Moderate parent')))
    user_adoption_counselling =  models.IntegerField(choices=((1,'No, I am an expert'),(2,'Yes, that will be lovely'),
                                                              (3,'Not sure about my time yet')))
    user_medical_history =  models.IntegerField(choices=((1,'Yes'),(2,'NO'),(3,'Never'),(4,'Not Sure')))
    user_callback = models.IntegerField(choices =((1,'Yes'),(2,'Definitely a yes'),
                                                  (3,'Does not look like I have an option so YES')))

    class Meta:
        db_table = "questionnaire"

    def __str__(self):
        return self.user_id.user_first_name


####################### pet ##########################################

class pet(models.Model):
    pet_id = models.AutoField(primary_key = True)
    pet_name = models.CharField(max_length = 30, null = True)
    pet_birthday = models.DateField(max_length=8)                #import birthday
    pet_type = models.CharField(max_length = 30)
    pet_breed = models.CharField(max_length = 30)
    pet_gender = models.IntegerField(choices = ((0,'Male'),(1,'Female')))
    pet_age = models.IntegerField()
    pet_images = models.ImageField(upload_to='pet', blank = True, null = True)
    pet_bio = models.TextField(max_length = 500)
    pet_owner = models.ForeignKey(owner, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = "pet"

    def __str__(self):
        return self.pet_name

####################### appointments ##########################################

#class Appointment(models.Model):
#    user = models.CharField(max_length=150)
#    phone_number = models.CharField(max_length=15)
#    time = models.DateTimeField()
#    time_zone = TimeZoneField(default='UTC')

#    # Additional fields not visible to users
#    task_id = models.CharField(max_length=50, blank=True, editable=False)
#    created = models.DateTimeField(auto_now_add=True)

#    def __str__(self):
#        return 'Appointment #{0} - {1}'.format(self.pk, self.name)

#    def get_absolute_url(self):
#        return reverse('view_appointment', args=[str(self.id)])