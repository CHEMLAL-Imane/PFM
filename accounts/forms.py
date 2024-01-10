from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList 
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class':'form-control',
        }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'confirm_password'
        }))
    class Meta :
        model= Account
        fields = ['first_name','last_name','phone_number','email','password']
    def __init__(self,*args, **kwargs):
            super(RegistrationForm,self).__init__(*args, **kwargs)
            self.fields['first_name'].widget.attrs['placeholder']='Enter first name'
            self.fields['last_name'].widget.attrs['placeholder']='last first name'
            self.fields['phone_number'].widget.attrs['placeholder']='Enter phone number'
            self.fields['email'].widget.attrs['placeholder']='Enter Address email'
            for field in self.fields :
                self.fields[field].widget.attrs['class']='form-control'
            
    def clean(self):
             
            cleaned_data = super(RegistrationForm, self).clean()
            password = cleaned_data.get('password')
            confirm_password = cleaned_data.get('confirm_password')
                  
            if password != confirm_password:
              raise forms.ValidationError("Password does not match! Try again")
            return cleaned_data
                