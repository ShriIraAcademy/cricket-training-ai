# tf_api/serializers.py
from rest_framework import serializers

class PredictionSerializer(serializers.Serializer):
    input_data = serializers.ListField(
        child=serializers.FloatField(),
        min_length=1
    )
