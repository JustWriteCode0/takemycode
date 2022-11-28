from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import UserCustom, Profile


class RegistrationForm(UserCreationForm):
   
    class Meta:
        model = UserCustom
        fields = ['username', 'email', 'password1', 'password2', 'user_avatar']

   
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name','describe' ,'github']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'user-profile-input'}),
            'last_name': forms.TextInput(attrs={'class': 'user-profile-input'}),
            'describe': forms.TextInput(attrs={'class': 'user-profile-input'}),
            'github': forms.URLInput(attrs={'class': 'user-profile-input'})
        }

