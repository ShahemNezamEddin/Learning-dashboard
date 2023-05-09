from django.test import TestCase
from .forms import *

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

    def test_is_finished_is_not_required(self):
        form = HomeworkForms({'subject': 'Test is_finished', 'title': 'Test is_finished', 'description': 'Test is_finished', 'due': '11-11-2023 11:11'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = HomeworkForms()
        self.assertEqual(form.Meta.fields, ['subject', 'title', 'description', 'due', 'is_finished'])

# Test Books and Wiki forms.


class TestDashboardForm(TestCase):

    def test_dashboard_text_is_required(self):
        form = DashboardForm({'text': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('subject', form.errors.keys())
        self.assertEqual(form.errors['subject'][0], 'This field is required.')

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
