from django.urls import path
from movies.views import HomepageView, ActorListView, MovieListView, MovieDetailView, \
    ActorDetailView, Jinja2TestingView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('actors/', ActorListView.as_view(), name='actors'),
    path('movies/', MovieListView.as_view(), name='movies'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('actor/<int:pk>/', ActorDetailView.as_view(), name='actor_detail'),
    path('testing/', Jinja2TestingView.as_view(), name='jinja2_testing_view'),
]
