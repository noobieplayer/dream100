from rest_framework import viewsets
from .models import Goaltag
from .serializers import GoaltagSerializer

# Create your views here.
class GoaltagViewSet(viewsets.ModelViewSet):
    queryset = Goaltag.objects.all()
    serializer_class = GoaltagSerializer