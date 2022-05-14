from datetime import timedelta

from django.contrib.auth.models import User
from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from django.utils import timezone
from model_bakery import baker

from movies.models import Movie, Actor
from movies.views import MovieListView


class TestURLS(SimpleTestCase):

    def test_movies_url_is_resolved_correctly(self):
        url = reverse('movies')
        self.assertEqual(resolve(url).func.view_class, MovieListView)


class TestViews(TestCase):
    def setUp(self):
        """ This method is run before every test_ method defined in the TestCase """
        self.user_1 = User.objects.create_superuser('JuckNorris', email='admin@admin.com', password='admin123456')
        self.client = Client()
        self.client.login(username='JuckNorris', password='admin123456')

        self.movie = baker.make(Movie)

    def test_homepage_is_working_correctly(self):
        homepage_url = reverse('homepage')
        response = self.client.get(homepage_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'homepage.html')

    def test_movie_detail_GET(self):
        detail_movie_url = reverse('movie_detail', args=[self.movie.id, ])
        response = self.client.get(detail_movie_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'movie_detail.html')

        detail_movie_url = reverse('movie_detail', args=[9999999999999, ])
        response = self.client.get(detail_movie_url)
        self.assertEqual(response.status_code, 404)

    def test_create_actor_success(self):
        create_actor_url = reverse('create_actor')
        data = {
            'name': 'TestActor',
            'age': 63,
            'gender': 'male',
            'born_at': (timezone.now() - timedelta(days=365*63)).date().isoformat(),
        }
        response = self.client.post(create_actor_url, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Actor.objects.filter(name=data['name']).exists())
