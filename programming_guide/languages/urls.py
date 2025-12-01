from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('popular/', views.popular_languages, name='popular'),
    path('language/<slug:slug>/', views.language_detail, name='language_detail'),
]