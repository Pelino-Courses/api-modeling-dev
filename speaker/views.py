from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .serializers import SpeakerSerializer
from .models import Speaker

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
