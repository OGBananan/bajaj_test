from rest_framework import serializers

class DataSerializer(serializers.Serializer):
    data = serializers.ListField(
        child=serializers.CharField(max_length=100)
    )
