from django import forms
from django.forms import ModelForm
from .models import displa

class displaForm(ModelForm):
	class Meta:
		model = displa
		fields = ('name', 'year', 'contact', 'email', 'material', 'price')
		labels={
            'name':'',
            'year': '',
            'contact': '',
            'email' : '',
            'material' : '',
            'price' : '',
         }
		widgets={
		    'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name here'}),
		    'year': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your year(FE/SE/TE/BE)'}),
		    'contact': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Insert your Mobile Number'}),
		    'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter your email id'}),
		    'material' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Decodes, EGR kits, Others (please specify)'}),
		    'price' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter amount in Rupee'}),
		 }