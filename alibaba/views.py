from django.http.response import HttpResponse , JsonResponse

def welcome(request):
    return HttpResponse('welcome to alibaba')


def about(request):
    return HttpResponse('about this page')

def flight(request):

    flight = {
      'flight_number':125115,
      'price' : 500.25 ,
      'emty_seat' : 30 ,
      'start ': 'iran' ,
       'destination ' : 'doubi'
    }
    
    return JsonResponse(flight)