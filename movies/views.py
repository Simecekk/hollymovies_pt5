from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views.generic import ListView, DetailView, TemplateView, FormView

from movies.forms import ContactForm
from movies.models import Movie, Actor, Director, Contact
from django.views import View


class HomepageView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'number_of_movies': Movie.objects.all().count(),
            'number_of_actors': Actor.objects.all().count(),
            'number_of_directors': Director.objects.all().count(),
            'page_name': 'Homepage'
        }
        return TemplateResponse(request, 'homepage.html', context=context)


# def homepage_view(request):
#     if request.method == 'GET':
#         context = {
#             'number_of_movies': Movie.objects.all().count(),
#             'number_of_actors': Actor.objects.all().count(),
#             'page_name': 'Homepage'
#         }
#         return TemplateResponse(request, 'homepage.html', context=context)
#     elif request.method == 'POST':
#         return HttpResponse(request, 'method not allowed')


class ActorListView(ListView):
    model = Actor
    template_name = 'actors.html'
    extra_context = {'page_name': 'Actors'}


class HollyMoviesDetailView(DetailView):
    def get_context_data(self, **kwargs):
        context = super(HollyMoviesDetailView, self).get_context_data(**kwargs)
        context.update({'page_name': self.object.name})
        return context


class ActorDetailView(HollyMoviesDetailView):
    model = Actor
    template_name = 'actor_detail.html'

# def actors_view(request):
#     actors = Actor.objects.all()
#     context = {
#         'all_actors': actors,
#         'page_name': 'Actors',
#     }
#     return TemplateResponse(request, 'actors.html', context=context)


class DirectorListView(ListView):
    model = Director
    template_name = 'directors.html'
    extra_context = {'page_name': 'Directors'}


class DirectorDetailView(HollyMoviesDetailView):
    model = Director
    template_name = 'actor_detail.html'


class MovieListView(ListView):
    queryset = Movie.objects.all().order_by('-rating')
    template_name = 'movies.html'
    extra_context = {
        'best_movies': Movie.objects.filter(rating__gte=80).order_by('-rating'),
        'worst_movies': Movie.objects.filter(rating__lte=20).order_by('rating'),
        'page_name': 'Movies',
    }


class MovieDetailView(HollyMoviesDetailView):
    model = Movie
    template_name = 'movie_detail.html'

    def post(self, request, pk, *args, **kwargs):
        movie = self.get_object()
        movie.likes += 1
        movie.save(update_fields=['likes', ])
        return redirect('movie_detail', pk=pk)


# def movies_view(request):
#     all_movies = Movie.objects.all().order_by('-rating')  # SELECT * FROM movies_movie;
#     best_movies = Movie.objects.filter(rating__gte=80).order_by('-rating')  # SELECT * FROM movies_movie WHERE rating GTE 80;
#     worst_movies = Movie.objects.filter(rating__lte=20).order_by('rating')
#     context = {
#         'all_movies': all_movies,
#         'best_movies': best_movies,
#         'worst_movies': worst_movies,
#         'page_name': 'Movies',
#     }
#     return TemplateResponse(request, 'movies.html', context=context)


class Jinja2TestingView(TemplateView):
    template_name = 'jinja2_testing.html'
    extra_context = {
        'testing_list': ['index_1', 'index_2', 'index_3'],
        'testing_dict': {'key_1': 'value_1', 'key_2': 'value_2'},
        'testing_queryset': Movie.objects.all(),
    }

# def jinja2_testing_view(request):
#     index_list = ['index_1', 'index_2', 'index_3']
#     index_1 = index_list[0]
#
#     testing_dict = {'key_1': 'value_1', 'key_2': 'value_2'}
#     value_1 = testing_dict['key_1']
#
#     context = {
#             'testing_list': index_list,
#             'testing_dict': testing_dict,
#             'testing_queryset': Movie.objects.all(),
#     }
#     return TemplateResponse(request, 'jinja2_testing.html', context=context)


# class ContactView(View):
#     def get(self, request, *args, **kwargs):
#         context = {
#             'contact_form': ContactForm()
#         }
#         return TemplateResponse(request, 'contact.html', context=context)
#
#     def post(self, request, *args, **kwargs):
#         bounded_form = ContactForm(request.POST)
#         if not bounded_form.is_valid():
#             return TemplateResponse(request, 'contact.html', context={'contact_form': bounded_form})
#
#         name = bounded_form.cleaned_data.get('name')
#         phone_number = bounded_form.cleaned_data.get('phone_number')
#         email = bounded_form.cleaned_data.get('email')
#         subject = bounded_form.cleaned_data.get('subject')
#         contact_at = bounded_form.cleaned_data.get('contact_at')
#
#         Contact.objects.create(
#             name=name,
#             phone_number=phone_number,
#             email=email,
#             subject=subject,
#             contact_at=contact_at
#         )
#
#         return TemplateResponse(request, 'contact.html', context={'contact_form': ContactForm()})

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        phone_number = form.cleaned_data.get('phone_number')
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        contact_at = form.cleaned_data.get('contact_at')

        Contact.objects.create(
            name=name,
            phone_number=phone_number,
            email=email,
            subject=subject,
            contact_at=contact_at
        )
        return TemplateResponse(self.request, 'contact.html', context={'form': ContactForm()})

    def form_invalid(self, form):
        return TemplateResponse(self.request, 'contact.html', context={'form': form})
