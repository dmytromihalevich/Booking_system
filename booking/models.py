from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TypeRoom(models.Model):
    name = models.CharField()
    discription = models.TextField(null=True, blank=True)


    def __str__(self):
        return f'Room type:{self.name}'


class Room(models.Model):
    type_room = models.ForeignKey(TypeRoom,on_delete=models.CASCADE,related_name='rooms')
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="rooms",null=True)
    price = models.IntegerField()
    discription = models.TextField(null=True, blank=True)
    places = models.IntegerField(default=1)



    def __str__(self):
        return f'Room:{self.name}, price:{self.price}'
    
class Booking(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE,related_name='bookings')
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='bookings')
    email = models.EmailField()
    date_in = models.DateTimeField()
    date_out = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20)


    def __str__(self):
        return f'Booking:{self.room},Date in:{self.date_in},Date out:{self.date_out}'
    