from django.conf.urls import url
from worker_info import views

app_name = 'worker_info'

urlpatterns = [
    url(r'All/',views.All,name='All'),
    url(r'Eletronics/',views.Eletronics,name='Eletronics'),
    url(r'Plumber/',views.Plumber,name='Plumber'),
    url(r'Carpenter/',views.Carpenter,name='Carpenter'),
    url(r'Contractor/',views.Contractor,name='Contractor'),
    url(r'Mechanic/',views.Mechanic,name='Mechanic'),
]
