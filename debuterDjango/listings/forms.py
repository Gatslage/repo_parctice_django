
from django import forms


class contactUsForm(forms.Form):
    name=forms.CharField(max_length=50,required=False)
    email=forms.EmailField(required=True)
    message=forms.CharField(required=True,max_length=250)