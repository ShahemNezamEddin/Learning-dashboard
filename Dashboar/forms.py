from django import forms
from . models import *


# Notes forms.


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']

