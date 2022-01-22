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
# generics view and mixins view
from rest_framework import generics
from rest_framework import mixins
# Authentication
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# ViewSet
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


class NewsViewSet(viewsets.ViewSet):
    def list(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = News.objects.all()
        news = get_object_or_404(queryset, pk=pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data)

    def update(self, request, pk=None):
        news = News.objects.get(pk=pk)
        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    lookup_field = 'id'

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class GenericNewsView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def get(self, request):
        return self.list(request)


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


class NewsDetails(APIView):
    def get_object(self, id):
        try:
            return News.objects.get(id=id)
        except News.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        news = self.get_object(id)
        serializer = NewsSerializer(news)
        return Response(serializer.data)

    def put(self, request, id):
        news = self.get_object(id)
        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        news = self.get_object(id)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
