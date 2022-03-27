from django.template.response import TemplateResponse
from movies.models import Movie


def homepage(request):
    all_movies = Movie.objects.all()
    best_movies = Movie.objects.filter(rating__gte=80)
    worst_movies = Movie.objects.filter(rating__lte=20)
    context = {
        'all_movies': all_movies,
        'best_movies': best_movies,
        'worst_movies': worst_movies,
    }
    return TemplateResponse(request, 'homepage.html', context=context)
