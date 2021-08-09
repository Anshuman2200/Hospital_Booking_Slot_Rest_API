from hospital_apis.viewsets import HospitalViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('patients',HospitalViewset)

