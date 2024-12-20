from rest_framework import viewsets
from .models import Goal
from .serializers import GoalSerializer

# Create your views here.
class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    