from django.urls import path
from .views import list , AirportList
from .views import (
    list, AirportList, CreateAirport,
    AirportView, AirportDelete, 
    AirportRetrieve, AirportUpdate,
    AirportView2
    )



urlpatterns = [
    path('list' , list , name='list'),
    path('airport-list', AirportList.as_view(), name='airport-list'),
    path('create-airport', CreateAirport.as_view(), name='create-airport'),
    path('airport', AirportView.as_view(), name='airport'),
    path('airport-delete/<int:pk>', AirportDelete.as_view(), name='airport-delete'),
    path('airport-retrieve/<int:pk>', AirportRetrieve.as_view(), name='airport-retrieve'),
    path('airport-update/<int:pk>', AirportUpdate.as_view(), name='airport-update'),
    path('airport2/<int:pk>', AirportView2.as_view(), name='airport2'),
]