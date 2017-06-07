from django.test import TestCase

# Create your tests here.

from unittest import *
from django.core.urlresolvers import reverse
from forms import *
from views import *

class Tests_account(unittest.TestCase):

    def test_User_register(self):
        email = forms.EmailField(label='Email Address')
        email2 = forms.EmailField(label='Confirm Email')
        self.assertEquals(email,email2)

    def setUp(self):
        self.username = User.objects.create_user()

    def test_register(self):
        User.objects.create(first_name='foo', last_name='bar')

    def test_no_user(self):
        response = self.client.get(reverse('This user does not exist'))
        self.assertTemplateNotUsed(response)
        self.failUnlessEqual(response.status_code, 302)

    def tests_login_views(self):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        
