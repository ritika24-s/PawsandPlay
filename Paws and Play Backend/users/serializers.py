from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer, SerializerMethodField, ValidationError
from .models import *

# converts to JSON
# validates data passed

class userloginSerializer(ModelSerializer):
    class Meta:
        model = user_login_details
        fields = '__all__'


#User = get_user_model()


#class UserCreateSerializer(ModelSerializer):
#    class Meta:
#        model = User
#        fields = [
#            'user_first_name',
#            #'password',
#            'user_email_id',
#        ]
#        extra_kwargs = {"password":
#                            {"write_only": True}
#                            }