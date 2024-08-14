from django.contrib import admin

from .models import NewsModel, CategoryModel, ContactModel


admin.site.register([NewsModel, CategoryModel, ContactModel])
