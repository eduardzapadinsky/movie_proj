from django.contrib import admin
from django.urls import path
from . import views
from .views import ShowAllActors, ShowAllDirectors, ShowOneDirector, ShowOneActor

urlpatterns = [
    path('', views.show_all_movies),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detailed'),
    path('directors', ShowAllDirectors.as_view()),
    # path('directors/<int:id_director>', views.show_one_director, name='director-detailed'),
    path('directors/<int:pk>', ShowOneDirector.as_view(), name='director-detailed'),
    path('actors', ShowAllActors.as_view()),
    # path('actors/<int:id_actor>', views.show_one_actor, name='actor-detailed'),
    path('actors/<int:pk>', ShowOneActor.as_view(), name='actor-detailed'),
]
