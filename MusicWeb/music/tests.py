from django.test import TestCase

# Create your tests here.
from django.core.urlresolvers import reverse
from django.views import generic
from unittest import *
import models
import views

class Tests_music_models(TestCase):

    def tests_song(self):
        artist_name = models.CharField(max_length=100)
        self.assertTrue(artist_name == len(artist_name)<100)
        self.assertFalse(artist_name != len(artist_name)>100)
        song_title = models.CharField(max_length=200)
        self.assertTrue(song_title == len(song_title)<200)
        self.assertFalse(song_title != len(song_title)>200)
        genre = models.CharField(max_length=100, null=True, blank=True)
        self.assertTrue(genre == len(genre)<100)
        self.assertFalse(genre != len(genre)>100)

class Tests_music_views(TestCase):

    def delete_music(self):
        response = self.SongDelete.get(reverse('remove_song', args=(song.id,)), follow=True)
        self.assertContains(response, 'Are you sure you want to remove')

    def update_music(self):
        response = self.client.get(reverse('artist_name', 'song_title', 'genre', 'file_type', 'song_logo'))
        self.assertContains(response, 'Update song')

    def test_string_representation(self):
        entry = Entry(title="My entry title")
        self.assertEqual(str(entry), entry.title)

class Test_model(TestCase):
    def test_my_test_model(self):
        self.assertTrue(song.objects.create(name='foo'))
