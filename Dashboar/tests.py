from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .forms import *

from .models import *
# from django.contrib.auth.models import Group

# Create your tests here.

# Test Notes forms.


class TestNotesForm(TestCase):

    def test_note_title_is_required(self):
        form = NotesForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_note_description_is_required(self):
        form = NotesForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = NotesForm()
        self.assertEqual(form.Meta.fields, ['title', 'description'])

# Test Homework forms.


class TestHomeworkForms(TestCase):

    def test_homework_subject_is_required(self):
        form = HomeworkForms({'subject': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('subject', form.errors.keys())
        self.assertEqual(form.errors['subject'][0], 'This field is required.')

    def test_homework_title_is_required(self):
        form = HomeworkForms({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_homework_description_is_required(self):
        form = HomeworkForms({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0], 'This field is required.')

    def test_homework_due_is_required(self):
        form = HomeworkForms({'due': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('due', form.errors.keys())
        self.assertEqual(form.errors['due'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = HomeworkForms()
        self.assertEqual(form.Meta.fields, ['subject', 'title', 'description', 'due', 'is_finished'])

# Test Registration forms.


class TestUserRegistrationForm(TestCase):

    def test_registration_username_is_required(self):
        form = UserRegistrationForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'This field is required.')

    def test_registration_password1_is_required(self):
        form = UserRegistrationForm({'password1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('password1', form.errors.keys())
        self.assertEqual(form.errors['password1'][0], 'This field is required.')

    def test_registration_password2_is_required(self):
        form = UserRegistrationForm({'password2': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors.keys())
        self.assertEqual(form.errors['password2'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = UserRegistrationForm()
        self.assertEqual(form.Meta.fields, ['username', 'password1', 'password2'])

# Test Home views.


class TestHomeViews(TestCase):

    def test_get_home(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/home.html')

# Test Notes views.


class TestNotesViews(TestCase):
    def test_setUp(self):
        username = 'testuser'
        password = 'testpass'
        User = get_user_model()
        user = User.objects.create_user(username, password=password)
        logged_in = self.client.login(username=username, password=password)

    def test_get_Notes(self):
        response = self.client.get('/notes')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/notes.html')

    def test_get_delete_note(self):
        note = Notes.objects.create(title='Test delete a note', description='Test delete a note')
        response = self.client.get(f'/notes/{note.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/notes.html')


# Test Books views.


class TestBooksViews(TestCase):

    def test_get_Books(self):
        response = self.client.get('/books')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/books.html')

# Test Wiki views.


class TestWikiViews(TestCase):

    def test_get_Wiki(self):
        response = self.client.get('/wiki')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/wiki.html')

# Test model.


class TestModels(TestCase):
    def test_setUp(self):
        username = 'testuser'
        password = 'testpass'
        User = get_user_model()
        user = User.objects.create_user(username, password=password)
        logged_in = self.client.login(username=username, password=password)

    def test_homework_is_finished_is_false(self):
        homework = Homework.objects.create(subject='Test is_finished', title='Test is_finished', description='Test is_finished', due='2023-05-13 11:11')
        self.assertFalse(homework.is_finished)
