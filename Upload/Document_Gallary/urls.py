from django.conf.urls import url
from Document_Gallary import views

app_name = 'Document_Gallary'

urlpatterns = [
    url(r'^$',views.uploadingImage,name='uploadingImage'),
]
