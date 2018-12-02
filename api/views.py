from .models import *
from rest_framework import generics
from django_filters import rest_framework as filters
from .serializers import *

# Create your views here.


class GeneListCreate(generics.ListCreateAPIView):
    queryset = Gene.objects.all()
    serializer_class = GeneSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ['geneid', 'symbol', 'description']


class ActivityListCreate(generics.ListCreateAPIView):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ['activityid', 'metabolism']


class DrugListCreate(generics.ListCreateAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ['drugid', 'name_brand', 'generic']


class RecommendationListCreate(generics.ListCreateAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ['recommendationid', 'recommendation',
                     'geneid__symbol', 'geneid__geneid', 'geneid__description', 'drugid__drugid', 'drugid__name_brand', 'drugid__generic', 'activityid__activityid', 'activityid__metabolism', ]


class PatientListCreate(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ['patientid', 'first',
                     'last', 'dob', 'address', 'city', 'state', 'zip', 'phone', 'email']


class PatientGeneticsListCreate(generics.ListCreateAPIView):
    queryset = PatientGenetics.objects.all()
    serializer_class = PatientGeneticsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ['patientid__patientid', 'patientid__first',
                     'patientid__last', 'geneid__geneid', 'geneid__symbol', 'activityid__activityid', 'activityid__metabolism', ]


class PrescriberListCreate(generics.ListCreateAPIView):
    queryset = Prescriber.objects.all()
    serializer_class = PrescriberSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ['prescriberid', 'first', 'last', 'title',
                     'address', 'city', 'state', 'zip', 'phone', 'email']


class PrescriptionListCreate(generics.ListCreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ['prescriptionid', 'prescriberid__prescriberid', 'prescriberid__first', 'prescriberid__last', 'patientid__patientid', 'patientid__last', 'patientid__first', 'drugid__drugid',
                     'drugid__name_brand', 'date', 'dose']
