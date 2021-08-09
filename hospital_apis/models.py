from django.db import models

# Create your models here.

class Hospital_apis(models.Model):
    _id = models.AutoField
    name = models.CharField(max_length=50, blank=False, default='')
    critical_level = models.CharField(max_length=5,blank=False, default='low')
    pincode = models.CharField(blank=False, max_length=6)
    hospital = models.CharField(max_length=70)
    time_slot_start = models.CharField(max_length=20,blank=False)
    time_slot_end = models.CharField(max_length=20,blank=False)