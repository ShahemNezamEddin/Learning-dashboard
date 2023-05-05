from django import forms
from . models import *
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm

# Notes forms.


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']

# Homework forms.


class DateInput(forms.DateInput):
    input_type = 'datetime'


class HomeworkForms(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due': DateInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'})}
        fields = ['subject', 'title', 'description', 'due', 'is_finished']

# Books and Wiki forms.


class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100, label='Enter search')

# Registration


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
