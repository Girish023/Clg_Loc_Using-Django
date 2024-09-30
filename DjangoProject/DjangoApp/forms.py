from django import forms
from .models import DjangoVarity



class DjangoVarityForm(forms.Form):
    Dj_Var=forms.ModelChoiceField(queryset=DjangoVarity.objects.all(),label="Select Django Varity")
