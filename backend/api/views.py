from django.shortcuts import render
from django.template import loader

from rest_framework.response import Response
# from rest_framework import status
from rest_framework.decorators import api_view

from pexels_api import API
from pydantic import BaseModel

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

# @api_view(['POST'])
# def select_image(request):