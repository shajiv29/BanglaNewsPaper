from django.urls import path
from .views import news_list, news_details, NewsAPIView

urlpatterns = [
    # Method based call
    # path('news/', news_list),
    path('news/', NewsAPIView.as_view()),
    path('detail/<int:pk>/', news_details),
]
