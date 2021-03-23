from rest_framework import serializers
from .models import *

# converts to JSON
# validates data passed

class adoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = adoption
        fields = '__all__'

