from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from .serializer import EventSerializer
from .models import Event
from django.http import JsonResponse


# Create your views here.

@api_view(['GET']) 
def get_Event(request):
    events=Event.objects.all()
    serializer=EventSerializer(events,many=True)    
    return JsonResponse(serializer.data, safe=False)



@api_view(['POST', 'GET']) 
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


@api_view(['GET']) 
def get_single_event(request, event_id):
    event = Event.objects.get(id=event_id)
    serializer=EventSerializer(event,many=False)
    return Response(serializer.data)