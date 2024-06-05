from django import forms
from bd.models import *


class StaffsForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'type', 'character', 'price', 'image']
