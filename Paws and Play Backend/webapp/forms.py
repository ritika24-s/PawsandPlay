from django import forms
#from django.contrib.auth.forms import ModelForm
from .models import *


STATUS_CHOICES= [
    ('1', 'Shortlisted'),
    ('2', 'Rejected'),
    ('3', 'Pending'),
 
    ]


class applicationUpdateForm(forms.ModelForm):
    application_status = forms.ChoiceField(choices = STATUS_CHOICES, required = True)
    class Meta:
        model = adoption_request
        fields = ['application_status']
