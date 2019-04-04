from django import forms
from Image_Gallary2.models import UserInfoModel,ImageModel

class UserInfoForm(forms.ModelForm):
    text = forms.CharField(max_length=128)
    description = forms.CharField(max_length=512)

    class Meta:
        model = UserInfoModel
        fields = ('text', 'description', )


class ImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple':True}),label='Image')
    class Meta:
        model = ImageModel
        fields = ('image', )
