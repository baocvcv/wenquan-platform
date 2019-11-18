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
            image.name = str(request.user) + str(timezone.now()) + '.jpg'
            s = ImageModel(image=image)
            s.save()
            return Response({'url': str(s.image.url)})
        else:
            return Response('Error')
