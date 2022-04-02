from django.template.response import TemplateResponse
from movies.models import Movie, Actor


def homepage_view(request):
    context = {
        'number_of_movies': Movie.objects.all().count(),
        'number_of_actors': Actor.objects.all().count(),
        'page_name': 'Homepage'
    }
    return TemplateResponse(request, 'homepage.html', context=context)


def actors_view(request):
    actors = Actor.objects.all()
    context = {
        'all_actors': actors,
        'page_name': 'Actors',
    }
    return TemplateResponse(request, 'actors.html', context=context)


def movies_view(request):
    all_movies = Movie.objects.all().order_by('-rating')  # SELECT * FROM movies_movie;
    best_movies = Movie.objects.filter(rating__gte=80).order_by('-rating')  # SELECT * FROM movies_movie WHERE rating GTE 80;
    worst_movies = Movie.objects.filter(rating__lte=20).order_by('rating')
    context = {
        'all_movies': all_movies,
        'best_movies': best_movies,
        'worst_movies': worst_movies,
        'page_name': 'Movies',
    }
    return TemplateResponse(request, 'movies.html', context=context)
