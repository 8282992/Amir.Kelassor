from django.db import models

class Airport(models.Model):
    name = models.CharField(max_length=100)
    no = models.IntegerField()
    city = models.CharField(max_length=10)
    address = models.TextField()
    phone_number = models.IntegerField()
    open_time = models.TimeField()
    close_time  = models.TimeField()


class Flight (models.Model):
    origin = models.ForeignKey(Airport,on_delete=models.CASCADE)
    flight_number = models.CharField(max_length=25)
    price = models.FloatField()
    emty_seat = models.IntegerField()
    start = models.CharField(max_length=10)
    destination = models.CharField(max_length=10)


class Tickect(models.Model):
    name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    national_id = models.IntegerField()
    seat_number = models.IntegerField()
    email = models.EmailField()