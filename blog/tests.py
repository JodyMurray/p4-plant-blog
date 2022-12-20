from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase


User = get_user_model()


class TestViews(TestCase):
    def setUp(self):
        user_a = User(username='admin', email='jjkittymurray@gmail.com')
        user_a_pw = 'some_123_password'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.save()
        user_a.set_password(user_a_pw)
        self.user_a = user_a

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)

    def test_user_password(self):
        self.assertTrue(self.user_a.check_password(
            self.user_a_pw
            ))
    
    def test_login_url(self):
        login_url = settings.LOGIN_URL
        data = {"username": "admin", "password": self.user_a_pw}
        response = self.client.post("/accounts/login", data, follow=True)
        status_code = response.status_code
        redirect_path = response.get("PATH_INFO")
        # self.assertEqual(redirect_path, settings.LOGIN_REDIRECT_URL)
        self.assertEqual(status_code, 200)
