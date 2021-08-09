from rest_framework import viewsets
from . import models
from . import serializers

class HospitalViewset(viewsets.ModelViewSet):
    queryset = models.Hospital_apis.objects.all()
    serializer_class = serializers.HospitalSerializer

# All CRUD operations can be performed by this viewset.