from .models import *


from django import forms

class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        exclude = ['slug']
        fields = ['title', 'image', 'description']


class About(forms.ModelForm):

    class Meta:
        model = About
        fields = ['title', 'image', 'description']
        exclude = []


