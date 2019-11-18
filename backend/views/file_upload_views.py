"""Views for upload files"""
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone

from backend.models.file_upload import ImageModel


class ImageUploadView(APIView):
    """Views for upload image"""
    def post(self, request):
        """upload_image"""
        if 'imagefile' in request.FILES:
            image = request.FILES["imagefile"]
            name = str(request.user) + str(timezone.now()) + '.jpg'
            print(name)
            image.name = name.replace("_", "").replace(" ", "")
            print(image.name)
            instance = ImageModel(image=image)
            instance.save()
            return Response({'url': str(instance.image.url)})
        return Response('Error', status=400)
