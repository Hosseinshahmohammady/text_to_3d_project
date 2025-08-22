from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django.shortcuts import render



class TextTo3DAPIView(APIView):
    def post(self, request):
        prompt = request.data.get("text")
        headers = {
            "Authorization": "Bearer msy_lSiXV2MMtFmsAhB3zF8VfwiSOiqI3MuwXLtw",
            "Content-Type": "application/json"
        }
        data = {"prompt": prompt}
        response = requests.post("https://api.meshy.ai/v1/text-to-3d", headers=headers, json=data)
        
        model_url = response.json().get("model_url")
        return Response({"model_url": model_url})


def index(request):
    return render(request, 'generator/index.html')