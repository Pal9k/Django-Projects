from django.db import models

# Create your models here.
class InfoModel(models.Model):
    text = models.CharField(max_length=128)
    description = models.CharField(max_length=512)

class DOCModel(models.Model):
    user = models.ForeignKey(InfoModel, default=None, on_delete=None)
    doc = models.FileField(upload_to='doc/', blank=True, verbose_name='DOC')
