from rest_framework import serializers
from .models import *
class DataConverter(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'    #all data share by __all__ method
        
        