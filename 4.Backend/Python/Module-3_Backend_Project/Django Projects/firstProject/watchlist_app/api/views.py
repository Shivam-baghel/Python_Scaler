from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchlist_app.models import WatchList, StreamPlatform
from watchlist_app.api.serializers import WatchlistSerializer
from watchlist_app.api.streamPlatformSerializer import streamPlatformSerializer
from rest_framework import status


class StreamPlatformAV(APIView):
    
    def get(self, request):
        
        platform = StreamPlatform.objects.all()
        serializer = streamPlatformSerializer(platform, many = True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = streamPlatformSerializer(data= request.data)
        successResponse = "Data is saved successfully."
        responseData = {'return':successResponse}
        if serializer.is_valid():
            serializer.save()
            return Response(responseData, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StreamPlatformDetailAV(APIView):

    def get(self, request,id):
        try:
            platformById = StreamPlatform.objects.get(pk=id)
        except:
            return Response({'error':f"stream platform not found for id = {id}"}, status=status.HTTP_404_NOT_FOUND)
        # print(watchlistById)

        serializer = streamPlatformSerializer(platformById)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            platform = StreamPlatform.objects.get(pk=id)
        except:
            return Response({'error':f"Watchlist not found for id = {id}"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = streamPlatformSerializer(platform, data=request.data)
        successResponse = "Data is changed successfully."
        responseData = {'response':successResponse}
        if serializer.is_valid():
            serializer.save()
            return Response(responseData)
        else:
            return Response(serializer.errors)
        

    def delete(self, request, id):
        
        platform = StreamPlatform.objects.get(pk=id)
        successResponse = "Data is Deleted successfully."
        responseData = {'response':successResponse}
        platform.delete()
        return Response(responseData)    

class WatchListAV(APIView):
    
    def get(self, request):
        watchList = WatchList.objects.all()
        serializer = WatchlistSerializer(watchList, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
            
    def post(self, request):
        serializer = WatchlistSerializer(data= request.data)
        successResponse = "Data is saved successfully."
        responseData = {'return':successResponse}
        if serializer.is_valid():
            serializer.save()
            return Response(responseData, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class WatchListDetailAV(APIView):

    def get(self, request,id):
        try:
            watchlistById = WatchList.objects.get(pk=id)
        except:
            return Response({'error':f"Watchlist not found for id = {id}"}, status=status.HTTP_404_NOT_FOUND)
        print(watchlistById)

        serializer = WatchlistSerializer(watchlistById)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            watchlist = WatchList.objects.get(pk=id)
        except:
            return Response({'error':f"Watchlist not found for id = {id}"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchlistSerializer(WatchList, data=request.data)
        successResponse = "Data is changed successfully."
        responseData = {'response':successResponse}
        if serializer.is_valid():
            serializer.save()
            return Response(responseData)
        else:
            return Response(serializer.errors)
        

    def delete(self, request, id):
        
        watchlist = WatchList.objects.get(pk=id)
        successResponse = "Data is Deleted successfully."
        responseData = {'response':successResponse}
        watchlist.delete()
        return Response(responseData)  
        
# @api_view(['GET'])
# def Watchlist_list(request):
    
#     WatchlistsList = Watchlist.objects.all()
    
#     serializer = WatchlistSerializer(WatchlistsList, many = True)
    
#     return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['GET'])
# def WatchlistById(request,id):
#     try:
#         WatchlistById = Watchlist.objects.get(pk=id)
#     except:
#         return Response({'error':f"Watchlist not found for id = {id}"}, status=status.HTTP_404_NOT_FOUND)
#     print(WatchlistById)

#     serializer = WatchlistSerializer(WatchlistById)
    
#     return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['POST'])
# def addWatchlistDetails(request):
#     serializer = WatchlistSerializer(data= request.data)
#     successResponse = "Data is saved successfully."
#     responseData = {'return':successResponse}
#     if serializer.is_valid():
#         serializer.save()
#         return Response(responseData, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['PUT', 'DELETE'])
# def changeWatchlistState(request, id):
    
#     if request.method == 'PUT':
#         try:
#             Watchlist = Watchlist.objects.get(pk=id)
#         except:
#             return Response({'error':f"Watchlist not found for id = {id}"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = WatchlistSerializer(Watchlist, data=request.data)
#         successResponse = "Data is changed successfully."
#         responseData = {'response':successResponse}
#         if serializer.is_valid():
#             serializer.save()
#             return Response(responseData)
#         else:
#             return Response(serializer.errors)
        
#     else:
#         Watchlist = Watchlist.objects.get(pk=id)
#         successResponse = "Data is Deleted successfully."
#         responseData = {'response':successResponse}
#         Watchlist.delete()
#         return Response(responseData)
        