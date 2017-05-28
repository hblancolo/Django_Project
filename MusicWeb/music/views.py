from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Song

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_songs'

    def get_queryset(self):
        return Song.objects.all()

class DetailView(generic.DetailView):
    model = Song
    template_name = 'music/detail.html'


class SongCreate(LoginRequiredMixin, CreateView): # modelName_form is the template by default for this view
    login_url = '/accounts/login'
    redirect_field_name = 'redirect_to'
    model = Song
    fields = ['artist_name', 'song_title', 'genre', 'song_file', 'song_logo']


class SongUpdate(UpdateView):
    model = Song
    fields = ['artist_name', 'song_title', 'genre', 'file_type', 'song_logo']

# Actually i'm not using the delete function because I don't have any "Delete" button in html to assign it
class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('music:index')










