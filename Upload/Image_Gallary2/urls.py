from django.conf.urls import url
from Image_Gallary2 import views

app_name = 'Image_Gallary2'

urlpatterns = [
    url(r'Image_Gallary2/',views.uploadingImage,name='uploadingImage'),
]
