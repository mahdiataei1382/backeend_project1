from django.urls import path
from .views import news_list
urlpatterns = [
    path ("news_list" , news_list)
]
from django.urls import path 
from .views import news_list
from .views import filter_news_by_tags
from .views import post_new
urlpatterns = [
    path("news_list" , news_list),
    path('filter/', filter_news_by_tags),
    path('post_new/', post_new),
]
