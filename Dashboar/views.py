from django.shortcuts import render
from . models import *

# Create your views here.
# home views.


def home(request):
    return render(request, 'dashboard/home.html')

# home views.


def notes(request):
    notes = Notes.objects.filter(user=request.user)
    context = {'notes': notes}
    return render(request, 'dashboard/notes.html', context)
