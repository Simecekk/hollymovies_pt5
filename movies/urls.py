from django.urls import path
from movies.views import homepage_view, actors_view

urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('actors/', actors_view, name='all_actors')
]
