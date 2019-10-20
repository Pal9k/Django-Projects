from django.db import models

# Create your models here.
class job_info(models.Model):
    job_title = models.CharField(max_length=100)
    type = models.CharField(max_length=25)
    description = models.CharField(max_length=1500)
    add = models.CharField(max_length=1000)
    last_date = models.DateField()
    mobileno = models.IntegerField(default=999999999)
