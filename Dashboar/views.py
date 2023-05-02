from django.shortcuts import render
from . forms import *

# Create your views here.
# home views.


def home(request):
    return render(request, 'dashboard/home.html')

# home views.


def notes(request):
    form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {'notes': notes, 'form': form}
    return render(request, 'dashboard/notes.html', context)
