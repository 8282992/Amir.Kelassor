from django.http.response import HttpResponse , JsonResponse
from .serializers import AirportSerializer
from rest_framework import generics
from .models import Airport



def list(request):

    flight = {
      'flight_number':115125,
      'price' : 500.25  ,
      'emty_seat' : 30 ,
      'start ': 'iran' ,
       'destination ' : 'doubi'
    }
    
    return JsonResponse(flight)


class AirportList(generics.ListAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

class CreateAirport(generics.CreateAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class AirportView(generics.ListCreateAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class AirportDelete(generics.DestroyAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class AirportRetrieve(generics.RetrieveAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class AirportUpdate(generics.UpdateAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class AirportView2(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer