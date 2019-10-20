from django.conf.urls import url
from post import views

app_name = 'post'

urlpatterns = [
    url(r'form/',views.post_job,name='post_job'),
]
