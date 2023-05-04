from django import forms
from . models import *
from django.forms import widgets


# Notes forms.


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']

# Homework forms.


class DateInput(forms.DateInput):
    input_type = 'date'


class HomeworkForms(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due': DateInput()}
        fields = ['subject', 'title', 'description', 'due', 'is_finished']


# books and Wiki forms.

class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100, label='Enter search')
