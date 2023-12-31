from .models import Station
from rest_framework.serializers import ModelSerializer


class StationSerializer(ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'