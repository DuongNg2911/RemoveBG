from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework import views

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from pexels_api import API
from PIL import Image
import base64
import io

from .serializers import ImageSerializer
from .services.removebg import removebg

pexels_api = API('WfiYlkjX2Y5hj57eTJmTuJibNCaBzesBrV1Yl7eQor9V0Gyap6wDhaHJ') # Paste your api key here

# Create function-based views here.
@api_view(['GET'])
def get_image_by_topic(request, content):
    response = pexels_api.search(content)
    urls = [x['src']['original'] for x in response['photos']]
    return render(request, 'images.html', {'response_urls': urls})

@api_view(['GET'])
def get_image_by_popular(request):
    response = pexels_api.popular()
    urls = [x['src']['original'] for x in response['photos']]
    return render(request, 'images.html', {'response_urls': urls})

# Create class-based views here.
class MyUploadView(views.APIView):
    parser_classes = [MultiPartParser,]

    @swagger_auto_schema(
        operation_description='Image',
        request_body=ImageSerializer,
    )

    def post(self, request):
        # Code to handle file
        image = request.FILES['photo']
        image = Image.open(image)
        result = removebg.removebg(image)
        
        buffered = io.BytesIO()
        result.save(buffered, format="PNG")
        img_bytes = buffered.getvalue()

        base64_string= base64.b64encode(img_bytes).decode('utf-8')

        return render(request, 'remove.html', {'encoded_image': "data:image/png;base64 " + base64_string})