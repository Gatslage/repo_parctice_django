
from dataclasses import field, fields
import imp
from pyexpat import model
from django import forms
from listings.models import band,Listing

class contactUsForm(forms.Form):
    name=forms.CharField(max_length=50,required=False)
    email=forms.EmailField(required=True)
    message=forms.CharField(required=True,max_length=250)

class bandForm(forms.ModelForm):
    class Meta:
        model=band
        fields= '__all__'
class annonceForm(forms.ModelForm):
    class Meta:
        model=Listing
        fields='__all__'

class annonceFormMod(forms.ModelForm):
    class Meta :
        model=Listing
        exclude=('year','type','band')