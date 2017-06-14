from django.test import TestCase

# Create your tests here.

from unittest import *
from django.core.urlresolvers import reverse
from forms import *
from views import *

class Tests_account(unittest.TestCase):

    def test_UserRegisterForm(self):
        email = clean('AGH@edu.pl')
        email2 = clean('AGH@edu.pl')
        email3 = clean('Agh@edu.pl')
        self.assertEqual(email,email2)
        self.assertRaises((email, email3), 'Emails must match')

    def setUp(self):
        self.username = User.objects.create_user()

    def test_register(self):
        User.objects.create(first_name='foo', last_name='bar')

    def test_no_user(self):
        response = self.forms.get(reverse('This user does not exist'))
        self.assertTemplateNotUsed(response)
        self.failUnlessEqual(response.status_code, 302)

    def tests_login_views(self):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        self.assertEqual((username, password), user)

    def tests_passwords(self):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user1 = authenticate(username=username, password=password)
        user2 = authenticate(username=username, password=password)
        self.assertEqual(user1('password'), user2('password'))
       
