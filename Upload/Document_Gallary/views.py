from django.shortcuts import render
from django.forms import modelformset_factory
from django.template import RequestContext

from .models import DOCModel,InfoModel
from .forms import DOCForm,InfoForm

# Create your views here.
def uploadingImage(request):
    if request.method == "POST":
        docForm = DOCForm(request.FILES or None)
        infoFrom = InfoForm(request.POST)

        if docForm.is_valid() and infoFrom.is_valid():
            info_form = infoFrom.save()

            DOCs = []
            for file in request.FILES.getlist('doc'):
                files = DOCModel(user=info_form, doc=file)
                DOCs.append(files.doc)
                files.save()

            return render(request,'Document_Gallary/show_image.html',{'text':info_form.text,'description':info_form.description, 'docs':DOCs})
        else:
            print(docForm.errors)
            print(infoFrom.errors)
            print(docForm)
            print(infoFrom)
    else:
        infoFrom= InfoForm()
        docForm = DOCForm()
    return render(request,'Document_Gallary/upload_image.html',{'infoForm': infoFrom, 'docForm': docForm})
