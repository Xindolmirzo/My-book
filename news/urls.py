from django.urls import path

from .views import (
    HomeView, ContactView, NewsDetailView, CategoryDetailView
)


urlpatterns = [
    path('', view=HomeView.as_view(), name='home_page'),
    path('contact/', view=ContactView.as_view(), name='contact_page'),
    path('news-detail/<int:pk>/', view=NewsDetailView.as_view(), name='news_detail_page'),
    path('category-detail/<int:pk>/', view=CategoryDetailView.as_view(), name='category_detail_page')
]