from django import forms
from django.forms import widgets
from .models import user
from django.core import validators




class Studentregi(forms.ModelForm):
     class Meta:
        model=user
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }




    
 