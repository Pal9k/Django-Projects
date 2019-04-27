from django.db import models

# Create your models here.
class worker_info(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=15)
    mobileno = models.IntegerField(default=999999999)
    add = models.CharField(max_length=1000)
    stars = models.FloatField()
    status = models.IntegerField(default=0)
    
