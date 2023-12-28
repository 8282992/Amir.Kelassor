from django.db import models

class Terminal(models.Model):
    name = models.CharField(max_length=100)
    no = models.IntegerField()
    city = models.CharField(max_length=10)
    address = models.TextField()
    phone_number = models.IntegerField()
    open_time = models.TimeField()
    close_time  = models.TimeField()


class Bus(models.Model):
    origin = models.ForeignKey(Terminal,on_delete=models.CASCADE)
    destination = models.CharField(max_length=25)
    ticket_number = models.CharField(max_length=25)
    price = models.FloatField()
    emty_seat = models.IntegerField()
    name = models.CharField(max_length=10)
    type = models.CharField(max_length=10)