from django import forms
from tweet.models import Tweet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Tweet_form(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo' ]

class UserRegistration_form(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')         