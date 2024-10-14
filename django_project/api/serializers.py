from rest_framework import serializers
from .models import UserMessage  # Import your model

class UserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessage
        fields = '__all__'
