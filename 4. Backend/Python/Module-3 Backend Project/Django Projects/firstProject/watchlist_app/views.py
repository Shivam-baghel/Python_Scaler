# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse
# # Create your views here.

# def movie_list(request):
#     movies = Movie.objects.all()
#     print(movies.values())
    
#     data = {'movies ': list(movies.values())}
#     return JsonResponse(data)


# def movieById(request,id):
#     movies = Movie.objects.get(pk=id)
#     print(movies)
#     # movieList = list(movies.values())
#     # data = {}
#     # for movie in movieList:
#     #     if id == movie[0]:
#     #         data.update(movie)
#     # if not data:
#     #     return JsonResponse('There is not movie with id : {id}')
#     # else:
#     data = {
#         'id': movies.pk,
#         'name': movies.name,
#         'description': movies.description,
#         'active': movies.active
#     }
#     return JsonResponse(data)
    