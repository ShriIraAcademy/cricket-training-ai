# from django.shortcuts import render
# tf_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PredictionSerializer
from .model import model
import numpy as np

class PredictionView(APIView):
    def post(self, request):
        serializer = PredictionSerializer(data=request.data)
        
        if serializer.is_valid():
            input_data = serializer.validated_data['input_data']
            # Convert the input into the format expected by the model
            input_array = np.array([input_data])  # Reshape if needed
            # Run prediction
            prediction = model.predict(input_array)
            # Format the prediction result
            result = prediction.tolist()  # Convert NumPy array to list for JSON serialization
            return Response({"prediction": result}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
