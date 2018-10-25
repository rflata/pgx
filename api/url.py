from django.urls import path
from . import views
urlpatterns = [
    path('api/genes/', views.GenesListCreate.as_view()),
    path('api/activity/', views.ActivityListCreate.as_view()),
    path('api/genes/', views.DrugsListCreate.as_view()),
    path('api/drugs/', views.DrugsListCreate.as_view()),
    path('api/recommendations/', views.RecommendationListCreate.as_view()),
]
