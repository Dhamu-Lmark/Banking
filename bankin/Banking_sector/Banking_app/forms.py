from django import forms 
from .models import *
 
class Account_form(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = '__all__'
    
 
 
class Transfer_form(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = '__all__'
 