from django.contrib import admin
from django.urls import path, include

from ads import views
from ads.views import CategoriesListView, AdsListView

urlpatterns = [
    path('', views.index, name='index'),
    path('cat/', CategoriesListView.as_view(), name='cat'),
    path('ad/', AdsListView.as_view(), name='ad'),
]
