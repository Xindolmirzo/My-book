from django.shortcuts import render

from django.views import View
from .models import CategoryModel, NewsModel

class HomeView(View):
     def get(self, request):
          
          all_news_list = NewsModel.manager.all().order_by('-publish_time')[:6]
          uzb_news_list = NewsModel.manager.all().filter(category__name="O'zbekiston").order_by('-publish_time')[:6]
          world_news_list = NewsModel.manager.all().filter(category__name="Jahon").order_by('-publish_time')[:6]
          science_news_list = NewsModel.manager.all().filter(category__name="Fan-texnika").order_by('-publish_time')[:6]
          sport_news_list = NewsModel.manager.all().filter(category__name="Sport").order_by('-publish_time')[:6]

          context = {
               'all_news_list' : all_news_list,
               'uzb_news_list' : uzb_news_list,
               'world_news_list' : world_news_list,
               'science_news_list' : science_news_list,
               'sport_news_list' : sport_news_list
               }
         
          return render(request=request, template_name='news/home.html', context=context)


class ContactView(View):
     def get(self, request):

          category_list = CategoryModel.objects.all()
          all_news_list = NewsModel.manager.all().order_by('-publish_time')[:9]

          context = {
               'category_list' : category_list,
               'all_news_list' : all_news_list
          }

          return render(request=request, template_name='news/contact.html', context=context)


class NewsDetailView(View):
     def get(self, request, pk):
          news_detail = NewsModel.objects.get(pk=pk)
          category_list = CategoryModel.objects.all()
          all_news_list = NewsModel.manager.all().order_by('-publish_time')[:9]

          context = {
               'category_list' : category_list,
               'news_detail' : news_detail,
               'all_news_list' : all_news_list
          }

          return render(request=request, template_name='news/news_detail.html', context=context)


class CategoryDetailView(View):
     def get(self, request, pk):
          category_detail = CategoryModel.objects.get(pk=pk)
          news_list = NewsModel.manager.all().filter(category__name=category_detail).order_by('-publish_time')[:6]
          category_list = CategoryModel.objects.all()
          all_news_list = NewsModel.manager.all().order_by('-publish_time')[:9]

          context = {
               'category_list' : category_list,
               'category_detail' : category_detail,
               'news_list' : news_list,
               'all_news_list' : all_news_list
          }

          return render(request=request, template_name='news/category_detail.html', context=context)