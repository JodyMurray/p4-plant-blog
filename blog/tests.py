from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Profile, User


class TestViews(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(
            username='test_user',
            email='test_user@gmail.com',
            password='test_password')
        test_user.is_staff = True
        test_user.is_superuser = True
        test_user.save()
        self.test_user = test_user
        test_profile = Profile.objects.create(
            id=1,
            user=test_user,
            first_name='test first name',
            last_name='test last name',
            bio='test bio'
        )

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(
            user_count,
            1
        )

    def test_login_url(self):
        login_url = settings.LOGIN_URL
        data = {
            'username': 'test_user',
            'password': 'test_password'
        }
        response = self.client.post(
            '/accounts/login',
            data,
            follow=True
        )
        status_code = response.status_code
        redirect_path = response.get('PATH_INFO')
        # self.assertEqual(redirect_path, settings.LOGIN_REDIRECT_URL)
        self.assertEqual(
            status_code,
            200
        )

    def test_get_user_profile(self):
        test_model = Profile.objects.get(
            bio='test bio'
        )
        response = self.client.get(
            '/profile/',
        )
        self.assertEqual(
            response.status_code,
            302
        )
