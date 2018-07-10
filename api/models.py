from django.db import models
from geopy import distance

# Create your models here.


class Hour(models.Model):
    status = models.TextField(unique=True)
    status_text = models.TextField()
    is_open = models.BooleanField()
    is_local_holiday = models.BooleanField()


class Restaurant(models.Model):
    name = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()
    hour = models.ForeignKey(Hour, on_delete=models.DO_NOTHING, null=True, blank=True)
    website = models.URLField(blank=True, null=True)
    place_id = models.TextField(default='', unique=True)

    def __str__(self):
        return self.name

    def is_in_range(self, user_location, radius):
        office_location = (self.lat, self.lng)
        distance_km = distance.vincenty(user_location, office_location).km
        return distance_km <= radius


class Photo(models.Model):
    photo_id = models.TextField(unique=True)
    prefix = models.URLField()
    suffix = models.TextField()
    width = models.IntegerField()
    height = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='photos')
