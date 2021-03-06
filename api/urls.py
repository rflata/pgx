from django.urls import path
from . import views
urlpatterns = [
    path('api/activity/',
         views.ActivityListCreate.as_view()),
    path('api/gene/', views.GeneListCreate.as_view()),
    path('api/drug/', views.DrugListCreate.as_view()),
    path('api/recommendation/', views.RecommendationListCreate.as_view()),
    path('api/patient', views.PatientListCreate.as_view()),
    path('api/patientgenetics', views.PatientGeneticsListCreate.as_view()),
    path('api/prescriber', views.PrescriberListCreate.as_view()),
    path('api/prescription', views.PrescriptionListCreate.as_view()),
]
