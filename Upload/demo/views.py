from django.shortcuts import render
from django.forms import modelformset_factory
from django.template import RequestContext

from .models import ImageModel,UserInfoModel
from .forms import ImageForm,UserInfoForm

# Create your views here.
def uploadingImage(request):
    if request.method == "POST":
        imageForm = ImageForm(request.POST or None,request.FILES or None)
        userFrom = UserInfoForm(request.POST)

        if imageForm.is_valid() and userFrom.is_valid():
            user_form = userFrom.save()

            images = []
            for img in request.FILES.getlist('image'):
                photo = ImageModel(user=user_form, image=img)
                images.append(photo.image)
                print(photo.image)
                photo.save()

            # print(type(user_form))
            # print(user_form.text)
            # print(user_form.description)
            # print(photo.imagemodel.all)
            # print(photo.user)
            print(photo.image)
            return render(request,'demo/show_image.html',{'text':user_form.text,'description':user_form.description, 'images':images})
        else:
            print("ERROR")
    else:
        userFrom= UserInfoForm()
        imageForm = ImageForm()
    return render(request,'demo/upload_image.html',{'userForm': userFrom, 'imageForm': imageForm})
