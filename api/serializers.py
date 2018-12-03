from .models import *

from rest_framework import serializers


class GeneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gene
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'

# Serializer for recommendation model imports foreign key relations


class RecommendationSerializer(serializers.ModelSerializer):
    geneid = GeneSerializer()
    drugid = DrugSerializer()
    activityid = ActivitySerializer()

    class Meta:
        model = Recommendation
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class PatientGeneticsSerializer(serializers.ModelSerializer):
    patientid = PatientSerializer()
    geneid = GeneSerializer()
    activityid = ActivitySerializer()

    class Meta:
        model = PatientGenetics
        fields = '__all__'


class PrescriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescriber
        fields = '__all__'


class PrescriptionSerializer(serializers.ModelSerializer):
    prescriberid = PrescriberSerializer()
    patientid = PatientSerializer()
    drugid = DrugSerializer()

    class Meta:
        model = Prescription
        fields = '__all__'
