# tf_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PredictionSerializer
from .model import model
import numpy as np

SHOTS = [
    {"name": "Straight Drive", "videolink": "https://youtu.be/8eb68_qqFHM?si=43OfKgsEMtgYqcjD"},
    {"name": "Pull Shot", "videolink": "https://youtu.be/g_Y_y4OHm1o?si=ejAO8C5cQW3Hb3Zz"},
    {"name": "Lofted Shot", "videolink": "https://youtu.be/QuiTxf_G-8A?si=BQL0Ic1uJwLhVWQ0"},
    {"name": "Cover Drive", "videolink": "https://youtu.be/JgGf_5LY6qA?si=1sRvstpzNXd6s15-"},
    {"name": "Hook Shot", "videolink": "https://youtu.be/quvpwDBViFg?si=v-74KSF3Zx0ySkK_"},
    {"name": "Sweep Shot", "videolink": "https://youtu.be/VAuatgBXwDA?si=ZGOsg3EbqtfZf4TL"},
    {"name": "Leg glance", "videolink": "https://youtu.be/7--nHWEqt_k?si=lYQvuwY4hzz6MMTh"},
    {"name": "square cut", "videolink": "https://youtu.be/8eb68_qqFHM?si=43OfKgsEMtgYqcjD"},
]
class PredictionView(APIView):
    def post(self, request):
        serializer = PredictionSerializer(data=request.data)
        
        if serializer.is_valid():
            input_data = serializer.validated_data['input_data']
            # Convert the input into the format expected by the model
            # input_array = np.array([input_data])  # Reshape if needed
            new_user = np.array(input_data)  # Reshape if needed
            # Run prediction
            # prediction = model.predict(input_array)
            predicted_ratings = model.predict([new_user[0], new_user[1], new_user[2], new_user[3]])
            # Format the prediction result
            # result = prediction.tolist()  # Convert NumPy array to list for JSON serialization
            # Get top 5 recommended cricket shots
            top_shots = np.argsort(predicted_ratings[0])[::-1][:5]  # Sort by rating and get top 5 shots
            print("Top recommended cricket shots indices:", top_shots)

            # return Response({"prediction": result}, status=status.HTTP_200_OK)
            return Response({"top_shots": [SHOTS[x] for x in top_shots]}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
