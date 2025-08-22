from django.urls import path
from .views import TextTo3DAPIView, index

urlpatterns = [
    path('', index, name='home'),
    path('api/generate/', TextTo3DAPIView.as_view(), name='generate_model'),
]
