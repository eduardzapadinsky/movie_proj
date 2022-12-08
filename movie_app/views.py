from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from django.views.generic import ListView, DetailView


# Create your views here.
def show_all_movies(request):
    # movies = Movie.objects.order_by(F('year').asc(nulls_last=True), 'rating')
    # movies = Movie.objects.filter(year__lt=2000)
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        str_field=Value("Hello, world"),
        int_field=Value(7),
        new_budget=F('year') / F('rating'),
    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg,
        'total': movies.count(),
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie,
    })


# def show_all_directors(request):
#     directors = Director.objects.all
#     return render(request, 'movie_app/all_directors.html', {
#         'directors': directors,
#     })


class ShowAllDirectors(ListView):
    template_name = 'movie_app/all_directors.html'
    model = Director
    context_object_name = 'directors'


class ShowOneDirector(DetailView):
    template_name = 'movie_app/one_director.html'
    model = Director


# def show_one_director(request, id_director: int):
#     director = get_object_or_404(Director, id=id_director)
#     return render(request, 'movie_app/one_director.html', {
#         'director': director,
#     })


# def show_one_actor(request, id_actor: int):
#     actor = get_object_or_404(Actor, id=id_actor)
#     return render(request, 'movie_app/one_actor.html', {
#         'actor': actor,
#     })


class ShowOneActor(DetailView):
    template_name = 'movie_app/one_actor.html'
    model = Actor


# def show_all_actors(request):
#     actors = Actor.objects.all
#     return render(request, 'movie_app/all_actors.html', {
#         'actors': actors,
#     })


class ShowAllActors(ListView):
    template_name = 'movie_app/all_actors.html'
    model = Actor
    context_object_name = 'actors'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_qs = queryset.filter(gender='M')
        return filter_qs
