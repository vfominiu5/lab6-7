from django.db import models


class UserModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)


class HotelModel(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    adress = models.CharField(max_length=30)
    description = models.CharField(max_length=255)


class BookingModel(models.Model):
    user_id = models.ForeignKey(UserModel)
    hotel_id = models.ForeignKey(HotelModel)
    price = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
