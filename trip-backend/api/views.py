from rest_framework.views import APIView
from rest_framework.response import Response
import sys
import os

# 👇 This makes Django able to read your model.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 👇 Import your ML function
from model import recommend_places   


class RecommendView(APIView):

    def post(self, request):
        try:
            data = request.data

            location = data.get("location")
            budget = int(data.get("budget", 20000))

            # 👇 Call your ML model
            result = recommend_places(location, budget)

            return Response({
                "success": True,
                "results": result
            })

        except Exception as e:
            return Response({
                "success": False,
                "error": str(e)
            })