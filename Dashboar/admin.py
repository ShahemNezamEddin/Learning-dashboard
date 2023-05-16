from django.contrib import admin
from . models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(Notes)
class NotesAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')
    search_fields = ['title']


@admin.register(Homework)
class HomeworkAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')
    list_filter = ('is_finished', 'due')
    search_fields = ['subject', 'title', 'description']
