from django.shortcuts import render
from django.shortcuts import redirect
from post.forms import postForm
from post.models import job_info

from worker_info import views
# Create your views here.
def index(request):
    records = job_info.objects.all().reverse()
    return render(request,'index.html',{'records':records})

def post_job(request):
    form = postForm()

    if request.method == "POST":
        form = postForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            print("SUCCESS !!!!!")
            return redirect(index)
        else:
            print("ERROR FROM INVALID")
            return redirect(index)
    return render(request,'post/post_job_form.html',{'form':form})
