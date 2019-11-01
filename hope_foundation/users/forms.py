from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()
	
	class Meta:
		model=CustomUser
		fields=['username','email','password1','password2']
