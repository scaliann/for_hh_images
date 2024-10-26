from rest_framework import viewsets
from .models import Image
from .serializers import ImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from PIL import Image as PILImage, ImageOps
from io import BytesIO
from django.core.files.base import ContentFile


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):

        instance = serializer.save()

        pil_image = PILImage.open(instance.file_path)
        gray_image = ImageOps.grayscale(pil_image)

        instance.size = gray_image.size[0] * gray_image.size[1]
        instance.resolution = f"{gray_image.width}x{gray_image.height}"
        instance.format = gray_image.format or pil_image.format

        gray_image_file = BytesIO()
        gray_image.save(gray_image_file, format=instance.format)
        instance.file_path.save(f"{instance.name}_gray.{instance.format.lower()}",
                                ContentFile(gray_image_file.getvalue()), save=False)


        resized_100 = gray_image.resize((100, 100))
        resized_500 = gray_image.resize((500, 500))


        resized_100_file = BytesIO()
        resized_500_file = BytesIO()
        resized_100.save(resized_100_file, format=instance.format)
        resized_500.save(resized_500_file, format=instance.format)

        instance.resized_100_path.save(f"{instance.name}_100x100.{instance.format.lower()}",
                                       ContentFile(resized_100_file.getvalue()), save=False)
        instance.resized_500_path.save(f"{instance.name}_500x500.{instance.format.lower()}",
                                       ContentFile(resized_500_file.getvalue()), save=False)


        gray_image_file.close()
        resized_100_file.close()
        resized_500_file.close()


        instance.save()
