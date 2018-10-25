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


class RecommendationSerializer(serializers.ModelSerializer):
    gene = GeneSerializer()
    drug = DrugSerializer()
    activity = ActivitySerializer()

    class Meta:
        model = Recommendation
        fields = '__all__'
