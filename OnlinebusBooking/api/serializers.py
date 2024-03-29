from rest_framework import serializers
from . models import *

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = '__all__'
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
