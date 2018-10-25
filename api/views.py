from .models import *
from rest_framework import generics
from .serializers import *

# Create your views here.


class GenesListCreate(generics.ListCreateAPIView):
    queryset = Genes.objects.all()
    serializer_class = GenesSerializer


class ActivityListCreate(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class DrugsListCreate(generics.ListCreateAPIView):
    queryset = Drugs.objects.all()
    serializer_class = DrugsSerializer


class RecommendationListCreate(generics.ListCreateAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
