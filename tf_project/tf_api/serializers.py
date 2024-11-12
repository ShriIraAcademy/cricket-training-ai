# tf_api/serializers.py
from rest_framework import serializers

class PredictionSerializer(serializers.Serializer):
    input_data = serializers.ListField(
        # child=serializers.FloatField(),
        child=serializers.ListField(child=serializers.IntegerField()),
        min_length=1
    )
