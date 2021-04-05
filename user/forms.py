from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class LoginForm(UserCreationForm):
    username = forms.CharField(label = "Kullanici Adi")
    password = forms.CharField(label = "Parola",widget = forms.PasswordInput)
    

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=32)
    first_name = forms.CharField(max_length=32)
    last_name=forms.CharField(max_length=32)
    email=forms.EmailField()


    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email','password1','password2']

