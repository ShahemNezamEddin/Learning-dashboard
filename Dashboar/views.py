from django.shortcuts import render, redirect, get_object_or_404
from . forms import *
from django.contrib import messages
from django.forms.widgets import FileInput
import requests
import wikipedia
from django.contrib.auth.decorators import login_required
from django.views import generic, View

# Create your views here.
# home views.


def home(request):
    return render(request, 'dashboard/home.html')


# home views.

@login_required
def notes(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user, title=request.POST['title'], description=request.POST['description'])
            notes.save()
        return redirect('/notes')
        messages.success(request, f"Note added from {request.user.username} successfully!")
    else:
        form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {'notes': notes, 'form': form}
    return render(request, 'dashboard/notes.html', context)

@login_required
def delete_note(request, pk=None):
    Notes.objects.get(id=pk).delete()
    messages.success(request, f"Note removed by {request.user.username} successfully!")
    return redirect("notes")

@login_required
def delete_note_confirm(request, pk=None):
    note = Notes.objects.get(id=pk)
    return render(request, "dashboard/delete_note_confirm.html", {"note": note})


@login_required 
def note_detail(request, pk=None):
    note = Notes.objects.get(id=pk)
    return render(request, "dashboard/note_detail.html", {"note": note})


# homework views.

@login_required
def homework(request):
    if request.method == 'POST':
        form = HomeworkForms(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False              
            except:
                finished = False

            Homeworks = Homework(
                user=request.user,
                subject=request.POST['subject'],
                title=request.POST['title'],
                description=request.POST['description'],
                due=request.POST['due'],
                is_finished=finished,
            )
            Homeworks.save()
            messages.success(request, f"Homework added from {request.user.username} successfully!")
    else:
        form = HomeworkForms()
    homework = Homework.objects.filter(user=request.user)
    if len(homework) == 0:
        homework_done = True
    else:
        homework_done = False

    context = {
        'homeworks': homework,
        'homeworks_done': homework_done,
        'form': form,
    }
    return render(request, 'dashboard/homework.html', context)

@login_required
def update_homework(request, pk=None):
    homework = Homework.objects.get(id=pk)
    if homework.is_finished:
        homework.is_finished = False
    else:
        homework.is_finished = True

    homework.save()
    return redirect('homework')

@login_required
def delete_homework(request, pk=None):
    Homework.objects.get(id=pk).delete()
    messages.success(request, f"Homework removed by {request.user.username} successfully!")
    return redirect("homework")


# Books views.

def books(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        text = request.POST['text']
        url = "https://www.googleapis.com/books/v1/volumes?q="+text
        r = requests.get(url)
        answer = r.json()
        result_list = []
        for i in range(10):
            result_dict = {
                'title': answer['items'][i]['volumeInfo']['title'],
                'subtitle': answer['items'][i]['volumeInfo'].get('subtitle'),
                'description': answer['items'][i]['volumeInfo'].get('description'),
                'count': answer['items'][i]['volumeInfo'].get('pageCount'),
                'categories': answer['items'][i]['volumeInfo'].get('categories'),
                'rating': answer['items'][i]['volumeInfo'].get('pageRating'),
                'thumbnail': answer['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                'preview': answer['items'][i]['volumeInfo'].get('previewLink')
            }
            result_list.append(result_dict)
            context = {
                'form': form,
                'results': result_list
                }
        return render(request, 'dashboard/books.html', context)

    else:
        form = DashboardForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/books.html', context)

# Wiki views.


def wiki(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        text = request.POST['text']
        search = wikipedia.page(text)
        context = {
            'form': form,
            'title': search.title,
            'url': search.url,
            'details': search.summary,
        }  
        return render(request, 'dashboard/wiki.html', context)
    else:
        form = DashboardForm()
        context = {
            'form': form
        }
    return render(request, 'dashboard/wiki.html', context)

# Register views.


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!!")
            return redirect("login")
    else:
        form = UserRegistrationForm
    context = {
        'form': form,
    }
    return render(request, 'dashboard/register.html', context)
