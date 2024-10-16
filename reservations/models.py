from django.db import models
from django.conf import settings


class Reservation(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    table_number = models.IntegerField()  
    date = models.DateField()  
    time = models.TimeField()  
    number_of_guests = models.IntegerField()  

    def __str__(self):
        return f'Reservation by {self.customer.username} on {self.date} at {self.time}'

