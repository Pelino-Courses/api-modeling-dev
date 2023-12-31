from rest_framework import serializers
from .models import Speaker

class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = ["id","name","biography","photo","email","phone_number","linkedin","twitter","instagram"]
