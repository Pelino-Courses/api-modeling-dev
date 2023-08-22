from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from .serializer import EventSerializer


# Create your views here.


def get_Event():
    pass

@api_view(['POST']) 
@csrf_exempt
def create_Event(request):
    data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'start_date': request.data.get('start_date'),
            'end_date': request.data.get('end_date'),
            'location':request.data.get('location'),
            'is_free': request.data.get('is_free'),
            'entry_fee': request.data.get('entry_fee'),
        }
    serializer=EventSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)