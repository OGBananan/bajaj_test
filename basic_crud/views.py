from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DataSerializer
from datetime import datetime

class BFHLAPIView(APIView):
    def post(self, request):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data['data']
            numbers = [item for item in data if item.isdigit()]
            alphabets = [item for item in data if item.isalpha()]
            lowercase_alphabets = [char for char in alphabets if char.islower()]
            highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None

            response = {
                "is_success": True,
                "user_id": "john_doe_17091999",
                "email": "john@xyz.com",
                "roll_number": "ABCD123",
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response({"operation_code": 1}, status=status.HTTP_200_OK)
