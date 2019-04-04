from django.db import models

# Create your models here.
class InfoModel(models.Model):
    text = models.CharField(max_length=128)
    description = models.CharField(max_length=512)

class PPTModel(models.Model):
    user = models.ForeignKey(InfoModel, default=None, on_delete=None)
    ppt = models.FileField(upload_to='ppt/', blank=True, verbose_name='PPT')
