from django.db import models

# Create your models here.
from django.db import models

class DataPoint(models.Model):
    name = models.CharField(max_length=100)
    size = models.FloatField()
    compression_type = models.CharField(max_length=50)
