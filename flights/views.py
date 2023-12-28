from django.http.response import HttpResponse , JsonResponse



def list(request):

    flight = {
      'flight_number':115125,
      'price' : 500.25  ,
      'emty_seat' : 30 ,
      'start ': 'iran' ,
       'destination ' : 'doubi'
    }
    
    return JsonResponse(flight)


