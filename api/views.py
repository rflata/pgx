from .models import *
from rest_framework import generics
from .serializers import *

# Create your views here.


class GeneListCreate(generics.ListCreateAPIView):
    queryset = Gene.objects.all()
    serializer_class = GeneSerializer


class ActivityListCreate(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class DrugListCreate(generics.ListCreateAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer


class RecommendationListCreate(generics.ListCreateAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
