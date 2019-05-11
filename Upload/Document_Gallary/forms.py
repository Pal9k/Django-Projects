from django import forms
from .models import InfoModel,DOCModel

class InfoForm(forms.ModelForm):
    text = forms.CharField(max_length=128)
    description = forms.CharField(max_length=512)

    class Meta:
        model = InfoModel
        fields = ('text', 'description', )


class DOCForm(forms.ModelForm):
    doc = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}),label='DOC',required=False)
    class Meta:
        model = DOCModel
        fields = ('doc', )
