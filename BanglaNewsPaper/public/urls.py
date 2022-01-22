from django.urls import path, include
from .views import news_list, news_details, NewsAPIView, NewsDetails, GenericAPIView, GenericNewsView, NewsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('news', NewsViewSet, basename='news')

urlpatterns = [
    # viewset url
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    # Method based call
    # path('news/', news_list),
    path('news/', NewsAPIView.as_view()),
    # path('detail/<int:pk>/', news_details),
    path('detail/<int:id>/', NewsDetails.as_view()),
    # path('generic/news/', GenericAPIView.as_view()),
    path('generic/news/<int:id>/', GenericAPIView.as_view()),
    path('generic/news/', GenericNewsView.as_view()),
]
