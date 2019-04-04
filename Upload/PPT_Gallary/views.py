from django.shortcuts import render
from django.forms import modelformset_factory
from django.template import RequestContext

from .models import PPTModel,InfoModel
from .forms import PPTForm,InfoForm

# Create your views here.
def uploadingImage(request):
    if request.method == "POST":
        pptForm = PPTForm(request.FILES or None)
        infoFrom = InfoForm(request.POST)

        if pptForm.is_valid() and infoFrom.is_valid():
            info_form = infoFrom.save()

            PPTs = []
            for file in request.FILES.getlist('ppt'):
                files = PPTModel(user=info_form, ppt=file)
                PPTs.append(files.ppt)
                files.save()

            return render(request,'PPT_Gallary/show_image.html',{'text':info_form.text,'description':info_form.description, 'ppts':PPTs})
        else:
            print(pptForm.errors)
            print(infoFrom.errors)
            print(pptForm)
            print(infoFrom)
    else:
        infoFrom= InfoForm()
        pptForm = PPTForm()
    return render(request,'PPT_Gallary/upload_image.html',{'infoForm': infoFrom, 'pptForm': pptForm})
