from django import forms
from .models import Image

class FindForm(forms.Form):
    find = forms.CharField(label='Find',required=False,widget = forms.TextInput(attrs={'class':'form-control'}))

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
        labels={
            'image' : 'デスクの画像'
        }