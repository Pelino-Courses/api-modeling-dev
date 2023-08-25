
from rest_framework import serializers
from Event.models import Event
from Event.models import Category

class EventSerializer(serializers.ModelSerializer):
   class Meta:
      model= Event
      fields='__all__'



class CategoryEventSerializer(serializers.ModelSerializer):
   class Meta:
      model=Category
      fields='__all__'
