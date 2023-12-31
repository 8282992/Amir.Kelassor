from django.shortcuts import render
from .serializers import StationSerializer
from rest_framework import generics 
from .models import Train

class Trainlist(generics.ListAPIView):
    queryset= Train.objects.all()
    serializer_class=StationSerializer

def train_list(request):
    pass