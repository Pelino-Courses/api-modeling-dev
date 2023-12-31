from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from .serializer import EventSerializer , CategoryEventSerializer
from .models import Event , Category
from django.http import JsonResponse


from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Create your views here.

@api_view(['GET']) 
def get_Event(request):
    events=Event.objects.all()
    serializer=EventSerializer(events,many=True)    
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET']) 
def get_Category(request):
    events=Category.objects.all()
    serializer=CategoryEventSerializer(events,many=True)    
    return JsonResponse(serializer.data, safe=False)



@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='string'),

    }
))
@api_view(['POST']) 
@csrf_exempt
def create_Category(request):
    data = {
            'name': request.data.get('name'),
        }
    serializer=CategoryEventSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'title': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'description': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'start_date': openapi.Schema(type=openapi.TYPE_STRING, description='date',format='date'),
        'end_date': openapi.Schema(type=openapi.TYPE_STRING, description='date',format='date'),
        'location': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'is_free': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='free or not free'),
        'entry_fee': openapi.Schema(type=openapi.TYPE_NUMBER, description='enter amount'),
         'category': openapi.Schema(type=openapi.TYPE_NUMBER, description='enter amount'),
    }    
))

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
            'category':request.data.get('category'),
        }
    serializer=EventSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET']) 
def get_single_event(request, event_id):
    event = Event.objects.get(id=event_id)
    serializer=EventSerializer(event,many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def EventDelete(request, pk):
    event = Event.objects.get(id = pk)
    event.delete()
    return Response("task deleted successfully.")

@swagger_auto_schema(method='put', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'title': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'description': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'start_date': openapi.Schema(type=openapi.TYPE_STRING, description='date',format='date'),
        'end_date': openapi.Schema(type=openapi.TYPE_STRING, description='date',format='date'),
        'location': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'is_free': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='free or not free'),
        'entry_fee': openapi.Schema(type=openapi.TYPE_NUMBER, description='enter amount'),
    }
))
@api_view(['PUT']) 
@csrf_exempt
def update_single_event(request, event_id):
    event =Event.objects.get(id=event_id)
    data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'start_date': request.data.get('start_date'),
            'end_date': request.data.get('end_date'),
            'location':request.data.get('location'),
            'is_free': request.data.get('is_free'),
            'entry_fee': request.data.get('entry_fee'),
        }
    serializer=EventSerializer(instance=event,data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)