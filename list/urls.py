from django.urls import path

from list.views import Notes, NoteCreate, NoteDelete

urlpatterns = [
    path('', Notes.as_view(), name='list'),
    path('note/create/', NoteCreate.as_view(), name='note_create'),
    path('note/delete/<int:pk>/', NoteDelete.as_view(), name='note_delete'),
]

