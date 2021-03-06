from django.db import models

# Create your models here.
class UserInfoModel(models.Model):
    text = models.CharField(max_length=128)
    description = models.CharField(max_length=512)

class ImageModel(models.Model):
    user = models.ForeignKey(UserInfoModel, default=None, on_delete=None)
    image = models.ImageField(upload_to='images/Image_Gallary2/', blank=True, verbose_name='Image')
