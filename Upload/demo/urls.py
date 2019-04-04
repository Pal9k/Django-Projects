from django.conf.urls import url
from demo import views

app_name = 'demo'

urlpatterns = [
    url(r'^$',views.uploadingImage,name='uploadingImage'),
]
