from django.forms import ModelForm

from list.models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ('text',)