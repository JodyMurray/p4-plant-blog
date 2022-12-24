from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import NewsLetter
from .forms import JoinForm
import datetime


class TestNewsletterView(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username='test_user',
            email='test_user@gmail.com',
            password='test_password'
        )
        test_newsletter = NewsLetter.objects.create(
            id=1,
            email='test_email@gmail.com',
            timestamp=datetime.date.today()
        )

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(
            user_count,
            1
        )

    def test_newsletter_exists(self):
        newsletter_count = NewsLetter.objects.all().count()
        self.assertEqual(
            newsletter_count,
            1
        )

    def test_newsletter_form(self):
        form_data = {
            'email': 'test_user@gmail.com',
        }
        newsletter_form = JoinForm(
            data=form_data
        )
        self.assertTrue(
            newsletter_form.is_valid()
        )
