from django import forms
from post.models import job_info

class postForm(forms.ModelForm):
    CHOICES = (
        ('Plumber', 'Plumber'),
        ('Carpenter', 'Carpenter'),
        ('Contractor', 'Contractor'),
        ('Eletronics', 'Eletronics'),
        ('Mechanic', 'Mechanic'),
    )
    type = forms.ChoiceField(choices=CHOICES)

    class Meta():
        model = job_info
        fields = "__all__"
