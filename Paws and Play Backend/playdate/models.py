from django.db import models

from users.models import pet, owner, user_login_details

# Create your models here.

class like(models.Model):
    user1_likes = models.ForeignKey(user_login_details, on_delete=models.CASCADE, related_name='user1_likes') 
    pet1_likes = models.ForeignKey(pet, on_delete=models.CASCADE, related_name='pet1')
    user2 = models.ForeignKey(user_login_details, on_delete=models.CASCADE, related_name='user2') 
    pet2 = models.ForeignKey(pet, on_delete=models.CASCADE, related_name='pet2')
    reaction = models.CharField(max_length = 1, choices = (('Y','Like'),('N','Dislike')))
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)

    class Meta:
        db_table = "like"


class match(models.Model):
    user1 = models.ForeignKey(user_login_details, on_delete=models.CASCADE, related_name='user1_matched') 
    pet1 = models.ForeignKey(pet, on_delete=models.CASCADE, related_name='pet1_matched')
    user2 = models.ForeignKey(user_login_details, on_delete=models.CASCADE, related_name='with_user2') 
    pet2 = models.ForeignKey(pet, on_delete=models.CASCADE, related_name='with_pet2')
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)

    class Meta:
        db_table = "match"