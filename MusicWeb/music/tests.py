from django.test import TestCase

# Create your tests here.
from django.core.urlresolvers import reverse
from unittest import *
from models import *
from views import *

class Tests_music(TestCase):
    def delete_music(self):
        response = self.client.get(reverse('remove_song', args=(song.id,)), follow=True)
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
