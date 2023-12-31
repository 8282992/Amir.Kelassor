from django.urls import path
from .views import Trainlist

urlpatterns = [
    path('trainlist', Trainlist.as_view(), name='tarin-list'),
]