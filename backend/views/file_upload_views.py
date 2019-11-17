from rest_framework.views import APIView
from rest_framework.response import Response

from backend.models.file_upload import ImageModel


class ImageUploadView(APIView):
    """Views for upload image"""
    def post(self, request):
        """upload_image"""
        if 'docfile' in request.FILES:
            image = request.FILES["docfile"]
            image.name = str(request.user) + str(time) + '.jpg'
            s = ImageModel(image=image)
            s.save()
            return Response({'url': str(s.image.url)})
        else:
            return Response('Error')
