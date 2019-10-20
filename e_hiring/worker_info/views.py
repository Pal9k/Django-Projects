from django.shortcuts import render
from worker_info.models import worker_info

# Create your views here.

def All(request):
    records = worker_info.objects.all()
    return render(request,'worker_info/category_query.html',{'records':records})

def Eletronics(request):
    myType = 'Eletronics'
    records = worker_info.objects.filter(type=myType)
    return render(request,'worker_info/category_query.html',{'records':records})

def Plumber(request):
    myType = 'Plumber'
    records = worker_info.objects.filter(type=myType)
    return render(request,'worker_info/category_query.html',{'records':records})

def Carpenter(request):
    myType = 'Carpenter'
    records = worker_info.objects.filter(type=myType)
    return render(request,'worker_info/category_query.html',{'records':records})

def Contractor(request):
    myType = 'Contractor'
    records = worker_info.objects.filter(type=myType)
    return render(request,'worker_info/category_query.html',{'records':records})

def Mechanic(request):
    myType = 'Mechanic'
    records = worker_info.objects.filter(type=myType)
    return render(request,'worker_info/category_query.html',{'records':records})
