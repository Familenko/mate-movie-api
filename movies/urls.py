from django.urls import path

from movies.views import movie_list_view, MovieListView, MovieListAPI

urlpatterns = [
    path("movies/", MovieListAPI.as_view(), name="movie_list_api"),
    # path('', MovieListView.as_view(), name='movie_list')
]

app_name = "movies"
