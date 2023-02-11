from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search_results, name='search_results'),
    path('', views.index, name='index'),
    path('impressum/', views.impressum, name='impressum'),
    path('data/', views.data, name='data')
]
