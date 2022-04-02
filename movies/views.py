from django.template.response import TemplateResponse
from movies.models import Movie


def homepage(request):
    all_movies = Movie.objects.all().order_by('-rating')  # SELECT * FROM movies_movie;
    best_movies = Movie.objects.filter(rating__gte=80).order_by('-rating')  # SELECT * FROM movies_movie WHERE rating GTE 80;
    worst_movies = Movie.objects.filter(rating__lte=20).order_by('rating')
    context = {
        'all_movies': all_movies,
        'best_movies': best_movies,
        'worst_movies': worst_movies,
    }
    return TemplateResponse(request, 'homepage.html', context=context)
