from django import forms
from .models import *


class UserOrderInfo(forms.ModelForm):
	class Meta:
		model = UOrder
		widgets = {
            'pname': forms.TextInput(attrs={'class': 'input',"placeholder":"Product Name"}),
            'email': forms.TextInput(attrs={'class': 'input',"placeholder":"Email"}),
            'address': forms.TextInput(attrs={'class': 'input',"placeholder":"Address"}),
            'city': forms.TextInput(attrs={'class': 'input',"placeholder":"City"}),
            'phonenumber': forms.TextInput(attrs={'class': 'input',"placeholder":"Phonenumber"}),
            'specfications': forms.TextInput(attrs={'class': 'input',"placeholder":"Specifications"}),
            'price': forms.TextInput(attrs={'class': 'input',"placeholder":"Price"})
        }
		fields = '__all__'







