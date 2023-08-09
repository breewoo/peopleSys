from django import forms
from . import models


class peopleform(forms.ModelForm):
    class Meta:
        model = models.People
        fields="__all__"