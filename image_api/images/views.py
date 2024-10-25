from rest_framework import viewsets
from .models import Image
from .serializers import ImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser]