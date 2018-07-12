from django import forms
# from django.forms import ModelForm
from .models import LandlordProfile


class LandlordForm(forms.ModelForm):
    class Meta:
        model = LandlordProfile
        exclude = []
        widgets = {}
