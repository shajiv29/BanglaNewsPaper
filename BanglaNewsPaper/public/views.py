from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import News
from .serializers import NewsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# class base api view
from rest_framework.views import APIView


class NewsAPIView(APIView):

    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







# @csrf_exempt
@api_view(['GET', 'POST'])
def news_list(request):
    if request.method == 'GET':
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        #       return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)


    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        #  serializer = NewsSerializer(data=data)
        serializer = NewsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #  return Response(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# This method using for only JSON response
# @csrf_exempt
# def news_details(request, pk):
#     try:
#         news = News.objects.get(pk=pk)
#     except News.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = NewsSerializer(news)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = NewsSerializer(news, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == "DELETE":
#         news.delete()
#         return HttpResponse(status=204)

# This method is using for only Django Rest api response
@api_view(['GET', 'PUT', 'DELETE'])
def news_details(request, pk):
    try:
        news = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NewsSerializer(news)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
