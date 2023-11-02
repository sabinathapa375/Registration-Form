from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import registration

class registrationForm(UserCreationForm):
    model=registration
    fields=['email','password1','password2']


class loginForm(forms.ModelForm):
    email= forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
