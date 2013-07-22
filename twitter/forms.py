from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Twitter

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserStatusForm(forms.ModelForm):
    class Meta:
        model = Twitter
        fields = ['status']
        widgets = {'status':forms.Textarea(attrs={'placeholder':'seu texto aqui'})}


