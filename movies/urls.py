from django.urls import path
from movies.views import HomepageView, ActorListView, MovieListView, jinja2_testing_view, MovieDetailView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('actors/', ActorListView.as_view(), name='actors'),
    path('movies/', MovieListView.as_view(), name='movies'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('testing/', jinja2_testing_view, name='jinja2_testing_view')
]
