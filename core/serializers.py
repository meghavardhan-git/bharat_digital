from rest_framework import serializers
from .models import DistrictData

class DistrictDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistrictData
        fields = '__all__'
