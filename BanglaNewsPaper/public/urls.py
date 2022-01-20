from django.urls import path
from .views import news_list, news_details

urlpatterns = [
    path('news/', news_list),
    path('detail/<int:pk>/', news_details),
]
