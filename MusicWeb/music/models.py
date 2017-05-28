from django.db import models
from django.core.urlresolvers import reverse

class Song(models.Model):
    artist_name = models.CharField(max_length=100)
    song_title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100, null=True, blank=True)
    song_file = models.FileField()
    song_logo=models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.song_title + ' - ' + self.artist_name




