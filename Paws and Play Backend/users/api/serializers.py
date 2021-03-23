from rest_framework.serializers import ModelSerializer , HyperlinkedIdentityField
#from rest_framework.serializers import SerializerMethodField
from ..models import *
from webapp.models import adoption_request


# converts to JSON
# validates data passed

########################### Views for owner ########################################

class ownerCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = owner
        fields = '__all__'


class ownerListSerializer(ModelSerializer):

    class Meta:
        model = owner
        fields = [
            'name',
            'photo',
            'sex',
            ]

class ownerRetrieveSerializer(ModelSerializer):

    class Meta:
        model = owner
        fields = [
            'name',
            'sex',
            'bio',
            'photo',
            'no_of_pets',
            ]


########################### Views for pet ########################################################

class petCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = pet
        fields = '__all__'


class petListSerializer(ModelSerializer):

    class Meta:
        model = pet
        fields = [
            'pet_name',
            'pet_type',
            'pet_breed',
            'pet_gender',
            ]

class petRetrieveSerializer(ModelSerializer):

    class Meta:
        model = owner
        fields = [
            'pet_name',
            'pet_type',
            'pet_breed',
            'pet_gender',
            'pet_age',
            'pet_images',
            'pet_bio',
            'pet_birthday',
            ]


########################### Serializers for questionnaire ########################################

#detail_url = HyperlinkedIdentityField(
#        view_name = 'user-api:questionnaire-detail',
#        lookup_field = 'pet_id',
#        )
#update_url = HyperlinkedIdentityField(
#        view_name = 'user-api:questionnaire-update',
#        lookup_field = 'pet_id',
#        )

class questionnaireListSerializer(ModelSerializer):
    #detail_url = detail_url
    #update_url = update_url

    class Meta:
        model = questionnaire
        fields = [
            #'detail_url'
            'user_fullname',
            'user_emailid',
            'user_contact_number',
            #'update_url',
            ]


class questionnaireCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = questionnaire
        fields = '__all__'


class questionnaireRetrieveSerializer(ModelSerializer):
    class Meta:
        model = questionnaire
        fields = '__all__'


class requestCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = adoption_request
        fields = '__all__'
