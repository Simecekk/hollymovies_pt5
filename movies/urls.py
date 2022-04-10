from django.urls import path
from movies.views import HomepageView, ActorListView, MovieListView, MovieDetailView, \
    ActorDetailView, Jinja2TestingView, DirectorListView, DirectorDetailView, ContactView, CreateMovieView, \
    CreateActorView, UpdateMovieView, UpdateActorView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('actors/', ActorListView.as_view(), name='actors'),
    path('movies/', MovieListView.as_view(), name='movies'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('actor/<int:pk>/', ActorDetailView.as_view(), name='actor_detail'),
    path('directors/', DirectorListView.as_view(), name='directors'),
    path('director/<int:pk>/', DirectorDetailView.as_view(), name='director_detail'),
    path('testing/', Jinja2TestingView.as_view(), name='jinja2_testing_view'),
    path('contact/', ContactView.as_view(), name='contact_view'),
    path('movie/create/', CreateMovieView.as_view(), name='create_movie'),
    path('actor/create/', CreateActorView.as_view(), name='create_actor'),
    path('movie/update/<int:pk>/', UpdateMovieView.as_view(), name='update_movie'),
    path('actor/update/<int:pk>/', UpdateActorView.as_view(), name='update_actor'),
]
