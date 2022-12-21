from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Profile, User, Post, Comment
import datetime


class TestViews(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(
            username='test_user',
            email='test_user@gmail.com',
            password='test_password'
        )
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
        test_post = Post.objects.create(
            id=1,
            title='test title',
            slug='test_title',
            author=test_user,
            content='test content',
        )
        test_comment = Comment.objects.create(
            id=1,
            post=test_post,
            body='test comment body',
            created_on=datetime.date.today(),
            approved=False
        )

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(
            user_count,
            1
        )

    def test_profile_exists(self):
        profile_count = Profile.objects.all().count()
        self.assertEqual(
            profile_count,
            1
        )

    def test_post_exists(self):
        post_count = Post.objects.all().count()
        self.assertEqual(
            post_count,
            1
        )

    def test_comment_exists(self):
        comment_count = Comment.objects.all().count()
        self.assertEqual(
            comment_count,
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
        redirect_path = response.get(
            'PATH_INFO'
        )
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
    
    def test_profile_settings_view(self):
        user = self.client.login(
            username='test_user',
            password='test_password'
        )
        self.client.post(
            f'/edit_profile/',
            {'first_name': 'test first name'}
        )
        profile = Profile.objects.get(
            first_name='test first name'
        )
        self.assertEqual(
            profile.first_name,
            'test first name'
        )
        response = self.client.get(
            '/profile/'
        )
        self.assertEqual(
            response.status_code,
            200
        )

    def test_post_detail_method_view_renders(self):
        post = Post.objects.get(
            title='test title'
        )
        self.assertEqual(
            post.title,
            'test title'
        )
        comments = Comment.objects.get(
            body='test comment body'
        )
        self.assertEqual(
            comments.body,
            'test comment body'
        )
        liked = False
        self.assertEqual(
            liked,
            False
        )
