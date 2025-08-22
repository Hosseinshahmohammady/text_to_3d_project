from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class TextTo3DAPIView(APIView):
    def post(self, request):
        prompt = request.data.get("text")
        headers = {
            "Authorization": "Bearer YOUR_MESHY_API_KEY",
            "Content-Type": "application/json"
        }
        data = {"prompt": prompt}
        response = requests.post("https://api.meshy.ai/v1/text-to-3d", headers=headers, json=data)
        
        model_url = response.json().get("model_url")
        return Response({"model_url": model_url})
