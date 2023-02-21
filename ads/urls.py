from django.contrib import admin
from django.urls import path, include

from ads import views

urlpatterns = [
    path('ad/', views.AdsListView.as_view(), name='ad'),
    path('ad/create/', views.AdsCreateView.as_view(), name='create_ad'),
    path('ad/<int:pk>/', views.AdsDetailView.as_view(), name='detail_ad'),
    path('ad/<int:pk>/update/', views.AdsUpdateView.as_view(), name='update_ad'),
    path('ad/<int:pk>/delete/', views.AdsDeleteView.as_view(), name='delete_ad'),

    path('cat/', views.CategoriesListView.as_view(), name='cat'),
    path('cat/create/', views.CategoriesCreateView.as_view(), name='create_cat'),
    path('cat/<int:pk>/', views.CategoriesDetailView.as_view(), name='detail_cat'),
    path('cat/<int:pk>/update/', views.CategoriesUpdateView.as_view(), name='update_cat'),
    path('cat/<int:pk>/delete/', views.CategoriesDeleteView.as_view(), name='delete_cat'),

]
