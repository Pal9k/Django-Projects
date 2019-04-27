import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE','e_hiring.settings')

import django
django.setup()

import random
from worker_info.models import worker_info
from faker import Faker

fakegen = Faker()
types = ['Eletronics','Carpenter','Plumber','Contractor','Mechanic']

def populate(N=5):
    for i in range(0,N):
        fake_name = fakegen.name()
        fake_type = random.choice(types)
        fake_mobileno = random.randint(000000000,999999999)
        fake_add = fakegen.address()
        fake_stars = round(random.uniform(0,5),1)
        fake_status = random.randint(0,30)

        obj_worker_info = worker_info.objects.get_or_create(name=fake_name,add=fake_add,type=fake_type,stars=fake_stars,status=fake_status,mobileno=fake_mobileno)

if __name__ == '__main__':
    print("populating script !!!")
    populate(20)
    print("populating complete !!!")
