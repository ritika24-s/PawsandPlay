from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from ..models import *

# converts to JSON
# validates data passed


########################### Serializers for vendor ########################################

#detail_url = HyperlinkedIdentityField(
#        view_name = 'vendor-api:vendor-detail',
#        lookup_field = 'vendor_username',
#        )
#update_url = HyperlinkedIdentityField(
#        view_name = 'vendor-api:vendor-update',
#        lookup_field = 'vendor_username',
#        )

class vendorListSerializer(ModelSerializer):
    #detail_url = detail_url
    #update_url = update_url
    #pet_adoption_centre_logo = SerializerMethodField()

    class Meta:
        model = vendor
        fields = [
            #'detail_url',
            'pet_adoption_centre_name',
            'pet_adoption_centre_logo',
            #'update_url',
            ]
    
    
    #def get_pet_adoption_centre_logo(self, obj):
    #    try:
    #        pet_adoption_centre_logo = obj.pet_adoption_centre_logo.url
    #    except:
    #        pet_adoption_centre_logo = None
    #    return pet_adoption_centre_logo


class vendorUpdateSerializer(ModelSerializer):
    class Meta:
        model = vendor
        fields = ['pet_adoption_centre_name','pet_adoption_centre_logo','vendor_contact','pet_adoption_location',
                  'pet_location_longitude','pet_location_latitude']


class vendorRetrieveSerializer(ModelSerializer):
    class Meta:
        model = vendor
        fields = '__all__'
        
        
class vendorCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(max_length=32,validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True, required=True, style={'input_type': 'password'})

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')