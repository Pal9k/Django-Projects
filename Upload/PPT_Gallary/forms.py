from django import forms
from .models import InfoModel,PPTModel

class InfoForm(forms.ModelForm):
    text = forms.CharField(max_length=128)
    description = forms.CharField(max_length=512)

    class Meta:
        model = InfoModel
        fields = ('text', 'description', )


class PPTForm(forms.ModelForm):
    ppt = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}),label='PPT',required=False)
    class Meta:
        model = PPTModel
        fields = ('ppt', )
