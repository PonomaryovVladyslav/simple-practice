# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView

from list.forms import NoteForm
from list.models import Note


class Notes(ListView):
    model = Note
    template_name = 'list/index.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(creator=self.request.user)
        if self.request.GET.get('search'):
            queryset = queryset.filter(text__icontains=self.request.GET.get('search'))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context.update({
            'note_form': NoteForm
        })
        return context


class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    http_method_names = ['post']
    success_url = '/'
    form_class = NoteForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)


class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    http_method_names = ['post']
    success_url = '/'
