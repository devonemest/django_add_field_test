from rest_framework import viewsets
from .models import Dummies
from .serializers import DummiesSerializer

class DummiesViewSet(viewsets.ModelViewSet):
    queryset = Dummies.objects.all()
    serializer_class = DummiesSerializer
