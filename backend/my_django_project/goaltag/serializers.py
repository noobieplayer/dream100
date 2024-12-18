from rest_framework import serializers
from .models import Goaltag

class GoaltagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goaltag
        fields = '__all__'