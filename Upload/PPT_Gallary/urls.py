from django.conf.urls import url
from PPT_Gallary import views

app_name = 'PPT_Gallary'

urlpatterns = [
    url(r'^$',views.uploadingImage,name='uploadingImage'),
]
