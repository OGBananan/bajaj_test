from django.urls import path
from .views import BFHLAPIView

urlpatterns = [
    path('bfhl/', BFHLAPIView.as_view(), name='bfhl'),
]

