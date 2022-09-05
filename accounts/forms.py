from django import forms 
from accounts.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username','email','password')

class RegistrationForm1(forms.ModelForm):

	class Meta:
		model = RegistrationModel
		fields = ('state','city')








# class LoginForm(forms.ModelForm):
# 	class Meta:
# 		model = LoginModel
# 		widgets = {
# 		"email":forms.TextInput(attrs={'placeholder': 'Email','class':'form-control bg-white  border-md '}),
# 		"password":forms.TextInput(attrs={'placeholder': 'Password','class':'form-control bg-white  border-md'})
# 		}
# 		fields = '__all__' 

# class RegisterForm(forms.ModelForm):
# 	class Meta:
# 		model = RegisterModel
# 		widgets = {
# 		"first_name":forms.TextInput(attrs={'placeholder':'First Name','class':'form-control bg-white  border-md '}),
# 		"last_name":forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control bg-white  border-md '}),
# 		"email":forms.TextInput(attrs={'placeholder':'Email','class':'form-control bg-white  border-md '}),
# 		"password":forms.TextInput(attrs={'placeholder':'Password','class':'form-control bg-white  border-md '})
# 		}
# 		fields = '__all__'







