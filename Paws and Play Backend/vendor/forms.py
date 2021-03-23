from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User


class vendorRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User           #vendor      
        fields = ['username', 'email', 'password1', 'password2']



###################################### update user name and email id ####################################
class UserUpdateForm(forms.ModelForm):
    #email = forms.EmailField()

    class Meta:
        model = User          #vendor
        fields = ['username', 'email']


class vendorUpdateForm(forms.ModelForm):

    class Meta:
        model = vendor
        
        fields = ['pet_adoption_centre_name', 'pet_adoption_centre_logo','vendor_contact','pet_adoption_location',
                  'pet_location_longitude','pet_location_latitude']


#def logout_view(request):
#    logout(request)
#    return render(request, "form.html", {})


