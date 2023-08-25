from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .serializers import ParticipantSerializer
from .models import Participant
import json
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='Eric Ndungutse'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='example@example.com'),
        'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='0785283007'),
        'events': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING) description='1')
    }
))
@csrf_exempt
@api_view(['GET', 'POST'])
def participants(request):
    if request.method == 'GET':
        participants = Participant.objects.all()
        serializer = ParticipantSerializer(participants, many=True)
        return Response(serializer.data, status=200)
    
    elif request.method == 'POST':
        participant = ParticipantSerializer(data=request.data)
        if participant.is_valid():
            participant.save()
            return Response(participant.data, status=201)
        return Response(participant.errors)

@swagger_auto_schema(method='patch', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='Eric Ndungutse'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='example@example.com'),
        'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='0785283007'),
        'events': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING) description='1')
    }
))
@api_view(['GET', 'DELETE', 'PATCH'])
def get_participant(request, id):
    # GET participant
    if request.method == 'GET':
        try:
            participant = Participant.objects.get(id=id)
            serializer = ParticipantSerializer(participant)
            return Response(serializer.data, status=200)

        except Participant.DoesNotExist:
            return Response("participant not found", status=404)

    # DELETE participant
    elif request.method == 'DELETE':
        try:
            participant = Participant.objects.get(id=id).delete()
            return Response("participant deleted", status=403)
        except participant.DoesNotExist:
            return Response("participant not found", status=404)
    
    elif request.method == 'PATCH':
        participant = Participant.objects.get(id=id)
        serializer = ParticipantSerializer(instance=participant, data=request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=200)
        
    return Response(participant.errors)
    

