from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .serializers import SpeakerSerializer
from .models import Speaker
import json
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'biography': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'photo': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'linkedin': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'twitter': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'instagram': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
    }
))
@csrf_exempt
@api_view(['GET', 'POST'])
def speakers(request):
    if request.method == 'GET':
        speakers = Speaker.objects.all()
        serializer = SpeakerSerializer(speakers, many=True)
        return Response(serializer.data, status=200)
    
    elif request.method == 'POST':
        speaker = SpeakerSerializer(data=request.data)
        if speaker.is_valid():
            speaker.save()
            return Response(speaker.data, status=201)
        return Response(speaker.errors)

@swagger_auto_schema(method='patch', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'biography': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'photo': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'linkedin': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'twitter': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'instagram': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
    }
))
@api_view(['GET', 'DELETE', 'PATCH'])
def get_speaker(request, id):
    # GET SPEAKER
    if request.method == 'GET':
        try:
            speaker = Speaker.objects.get(id=id)
            serializer = SpeakerSerializer(speaker)
            return Response(serializer.data, status=200)

        except Speaker.DoesNotExist:
            return Response("Speaker not found", status=404)

    # DELETE SPEAKER
    elif request.method == 'DELETE':
        try:
            speaker = Speaker.objects.get(id=id).delete()
            return Response("Speaker deleted", status=403)
        except Speaker.DoesNotExist:
            return Response("Speaker not found", status=404)
    
    elif request.method == 'PATCH':
        speaker = Speaker.objects.get(id=id)
        serializer = SpeakerSerializer(instance=speaker, data=request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=200)
        
    return Response(speaker.errors)
    

