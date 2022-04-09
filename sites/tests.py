from django import test as django_test
from django.contrib.auth import login
from django.urls import reverse

from sites.models import AppUsername, Post, AppUser


class TestHomeView(django_test.TestCase):

    def test_project_home(self):
        client = django_test.Client()

        response = client.get(reverse('home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_project_home_page_with_posts(self):
        client = django_test.Client()

        user = AppUser.objects.create(
            email='ilias.task@gmail.com',
            is_staff=False,
            is_superuser=False

        )
        p = Post.objects.create(
            title='random',
            details='random 2 test',
            category='Crypto',
            user=user

        )
        p.save()

        response = client.get(reverse('home'))

        posts = response.context['post']

        for p in posts:
            self.assertIsNotNone(p)

    def test_project_home_page_without_posts(self):
        client = django_test.Client()

        user = AppUser.objects.create(
            email='ilias.task@gmail.com',
            is_staff=False,
            is_superuser=False

        )

        response = client.get(reverse('home'))

        posts = response.context['post']
        self.assertEqual(posts.count(), 0)


class TestProfileMakePostView(django_test.TestCase):

    def test_post_page_without_profile_created(self):
        client = django_test.Client()

        response = client.get(reverse('post-make'), follow=True)

        self.assertTemplateUsed(response, 'login.html')

        self.assertEqual(200, response.status_code)

    def test_post_page_with_user(self):
        client = django_test.Client()
        user = AppUser.objects.create(
            email='ilias.task@gmail.com',
            is_staff=False,
            is_superuser=False

        )
        user.set_password('iliasgrbg15')
        user.save()
        app_user = AppUsername.objects.create(
            username='YoungTask',
            age=16,
            user=user
        )
        client.login(email='ilias.task@gmail.com',password = 'iliasgrbg15')

        response = client.get(reverse('post-make'), follow=True)
        self.assertTemplateUsed(response, 'make-post.html')
