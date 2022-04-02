from django.template.response import TemplateResponse
from movies.models import Movie, Actor


def homepage_view(request):
    context = {
        'number_of_movies': Movie.objects.all().count(),
        'number_of_actors': Actor.objects.all().count(),
    }
    return TemplateResponse(request, 'homepage.html', context=context)


def actors_view(request):
    actors = Actor.objects.all()
    context = {
        'all_actors': actors,
        'page_name': 'Actors',
    }
    return TemplateResponse(request, 'actors.html', context=context)


# all_movies = Movie.objects.all().order_by('-rating')  # SELECT * FROM movies_movie;
# best_movies = Movie.objects.filter(rating__gte=80).order_by('-rating')  # SELECT * FROM movies_movie WHERE rating GTE 80;
# worst_movies = Movie.objects.filter(rating__lte=20).order_by('rating')
# context = {
#     'all_movies': all_movies,
#     'best_movies': best_movies,
#     'worst_movies': worst_movies,
#     'page_name': 'Homepage',
# }


 #    <h4>All movies ({{ all_movies.count }})</h4>
 #    {% for movie in all_movies %}
 #        <p>{{ movie.name }} - rating ({{ movie.rating }})</p>
 #    {% endfor %}<br>
 #
 #
 #    <h4>Best movies ({{ best_movies.count }})</h4>
 #    {% for movie in best_movies %}
 #        <p>{{ movie.name }} - rating ({{ movie.rating }})</p>
 #    {% endfor %}<br>
 #
 #    <h4>Worst movies ({{ worst_movies.count }})</h4>
 #    {% for movie in worst_movies %}
 #        <p>{{ movie.name }} - rating ({{ movie.rating }})</p>
 #    {% endfor %}