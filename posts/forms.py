from .models import Publication
from django import forms


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'content', 'link', 'images']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'custom-input'}),
            'link': forms.URLInput(attrs={'placeholder': 'https://github.com/user/repository'}),
            'content': forms.Textarea(attrs={'rows':5, 'cols':5}),
        }