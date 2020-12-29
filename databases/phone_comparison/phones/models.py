from django.db import models

# Create your models here.


class Phone(models.Model):
    name = models.TextField()
    price = models.FloatField()
    has_3g = models.BooleanField()
    has_lte = models.BooleanField()
    sims_count = models.IntegerField()
    operational_system = models.TextField()
    ram = models.IntegerField()
    device_memory = models.IntegerField()
    processor = models.TextField()
    has_fm = models.BooleanField()
    has_bluetooth = models.BooleanField()
    has_gps = models.BooleanField()

