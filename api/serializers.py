from .models import Activity, Drugs, Genes, Recommendation

from rest_framework import serializers


class GenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genes
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class DrugsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drugs
        fields = '__all__'


class RecommendationSerializer(serializers.ModelSerializer):
    gene = GenesSerializer()
    drug = DrugsSerializer()
    activity = ActivitySerializer()

    class Meta:
        model = Recommendation
        fields = '__all__'
