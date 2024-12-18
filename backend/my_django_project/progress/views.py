from rest_framework import viewsets
from .models import Progress
from .serializers import ProgressSerializer

# Create your views here.
class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer