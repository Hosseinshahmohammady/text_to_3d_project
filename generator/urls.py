from django.urls import path
from .views import TextTo3DAPIView

urlpatterns = [
    path('api/generate/', TextTo3DAPIView.as_view(), name='generate_model'),
]
