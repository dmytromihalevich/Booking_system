from django.shortcuts import render

from booking.models import Room, Booking

# Create your views here.
def main_page(request):
    rooms = Room.objects.all()

    context = {
        "data":"hi from django",
        'room_list': rooms
    }

    return render(request, "booking/room_list.html", context)
    