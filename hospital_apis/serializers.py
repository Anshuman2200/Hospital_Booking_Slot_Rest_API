from rest_framework import serializers
from .models import Hospital_apis

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital_apis
        fields = '__all__'