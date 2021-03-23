from rest_framework.serializers import ModelSerializer , HyperlinkedIdentityField
#from rest_framework.serializers import SerializerMethodField
from ..models import *
from users.models import *

# converts to JSON
# validates data passed


########################### Serializers for adoption ########################################

detail_url = HyperlinkedIdentityField(
        view_name = 'adoption-api:adoption-detail',
        lookup_field = 'pet_id',
        )
update_url = HyperlinkedIdentityField(
        view_name = 'adoption-api:adoption-update',
        lookup_field = 'pet_id',
        )

class adoptionListSerializer(ModelSerializer):
    detail_url = detail_url
    update_url = update_url
    #image = SerializerMethodField()

    class Meta:
        model = adoption
        fields = [
            'detail_url',
            'pet_name',
            'pet_breed',
            'pet_type',
            'update_url',
            #'image'
            ]
    
    #def get_image(self, obj):
    #    try:
    #        image = obj.image.url
    #    except:
    #        image = None
    #    return image


class adoptionCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = adoption
        fields = '__all__'


class adoptionRetrieveSerializer(ModelSerializer):
    class Meta:
        model = adoption
        fields = '__all__'


class adoptionuserRetrieveSerializer(ModelSerializer):
    class Meta:
        model = adoption
        exclude = ['vendor_timestamp','vendor_update']


class adoptionuserListSerializer(ModelSerializer):
    class Meta:
        model = adoption
        fields = "__all__"



class userListSerializer(ModelSerializer):
    class Meta:
        model = user_login_details
        fields = "__all__"



class adoptionRequestListSerializer(ModelSerializer):
    user = userListSerializer(read_only=True)
    pet = adoptionuserListSerializer(read_only=True)            # change it to retrieve
    class Meta:
        model = adoption_request
        fields = ['id','user','pet','application_status','requested_at']