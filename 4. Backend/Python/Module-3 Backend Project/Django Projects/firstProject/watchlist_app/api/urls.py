from django.urls import path
# from watchlist_app.api.views import movie_list, movieById, addMovieDetails, changeMovieState
# from watchlist_app.api.views import MovieListAV,MovieDetailAV

from watchlist_app.api.views import WatchListDetailAV,WatchListAV, StreamPlatformAV, StreamPlatformDetailAV


urlpatterns = [

    path('list/',WatchListAV.as_view(), name='movie-list'),
    path('byId/<int:id>', WatchListDetailAV.as_view(), name= 'movie-by-id'),
    path('stream/', StreamPlatformAV.as_view(), name= 'steam-platform'),
    path('streamById/<int:id>', StreamPlatformDetailAV.as_view(), name= 'platform-by-id'),
    # path('addMovie/', addMovieDetails, name="add-Movie"),
    # path('updateMovie/<int:id>',changeMovieState, name = "updateMovie")
]



# urlpatterns = [

#     path('list/',movie_list, name='movie-list'),
#     path('byId/<int:id>', movieById, name= 'movie-by-id'),
#     path('addMovie/', addMovieDetails, name="add-Movie"),
#     path('updateMovie/<int:id>',changeMovieState, name = "updateMovie")
# ]
