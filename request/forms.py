from django import forms
from bd.models import *

class Application_forms(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'placeholder': 'Введите выдаваему сотруднику сумму'})


    class Meta:
        model = Application
        fields = ['worker', 'number_cab', 'description']


class ApplicationFormEdit(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['worker', 'number_cab', 'description']