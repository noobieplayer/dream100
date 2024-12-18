from rest_framework import viewsets
from .models import Tag
from .serializers import TagSerializer

# Create your views here.
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer