from django.db import models
class Station (models.Model):
    name = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    address = models.CharField(max_length=15)
    phone_number = models.IntegerField()
    open_time = models.TimeField()
    close_time = models.TimeField()

class Train (models.Model):
    origin = models.ForeignKey(Station,on_delete=models.CASCADE)
    destination = models.CharField(max_length=15)
    train_number = models.IntegerField()
    price = models.IntegerField()
    empty_seat = models.IntegerField()


