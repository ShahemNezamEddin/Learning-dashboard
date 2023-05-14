from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes', views.notes, name='notes'),
    path('delete_note/<int:pk>', views.delete_note, name='delete-note'),
    path('note_detail/<int:pk>', views.note_detail, name='note-detail'),
    path('delete_note_confirm/<int:pk>', views.delete_note_confirm, name='delete-note-confirm'),
    path('edit_note/<int:pk>', views.edit_note, name='edit-note'),

    path('homework', views.homework, name='homework'),
    path('update_homework/<int:pk>', views.update_homework, name='update-homework'),
    path('delete_homework/<int:pk>', views.delete_homework, name='delete-homework'),

    path('books', views.books, name='books'),

    path('wiki', views.wiki, name='wiki'),
    ]
