from django.conf.urls import url
from Image_Gallary1 import views

app_name = 'Image_Gallary1'

urlpatterns = [
    url(r'^$',views.versions,name='versions'),
    url(r'Image_Gallary1/',views.uploadingImage,name='uploadingImage'),
]
