from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Traveler)
class TravelerAdmin(admin.ModelAdmin):
    #fields = ('first_name', 'last_name')
    list_display = ('username','full_name','age','has_bookings',)
    list_filter = ('age',)
    search_fields = ['last_name', 'first_name']

    def full_name(self, obj):
        return "{} {}".format(obj.last_name, obj.first_name)

    def username(self, obj):
        return "{}".format(obj.user.username)

    def has_bookings(self, obj):
        hs = Booking.objects.filter(user=obj)
        return len(hs)>0


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
