from django.shortcuts import render
from .models import Image_GallaryModel

# Create your views here.
def uploadingImage(request):
    if request.method == 'POST':
        img=Image_GallaryModel()
        img.text = request.POST.get('txt')
        img.description = request.POST.get('description')

        images = []
        if 'img1' in request.FILES:
            img.img1=request.FILES.get('img1')
            images.append(img.img1)
        if 'img2' in request.FILES:
            img.img2=request.FILES.get('img2')
            images.append(img.img2)
        if 'img3' in request.FILES:
            img.img3=request.FILES.get('img3')
            images.append(img.img3)
        if 'img4' in request.FILES:
            img.img4=request.FILES.get('img4')
            images.append(img.img4)
        if 'img5' in request.FILES:
            img.img5=request.FILES.get('img5')
            images.append(img.img5)

        img.save()

        return render(request, 'Image_Gallary1/show_image.html', {'text':img.text,'description':img.description,'images':images})

    else:
        return render(request,'Image_Gallary1/upload_image.html')

    return render(request,'Image_Gallary1/upload_image1.html')

def versions(request):
    return render(request,'Image_Gallary1/versions_of_image.html')

def index(request):
    return render(request,'index.html')
