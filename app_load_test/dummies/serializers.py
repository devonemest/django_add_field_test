from rest_framework import serializers
from .models import Dummies

class DummiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dummies
        fields = ['id', 'name', 'height', 'weight']
