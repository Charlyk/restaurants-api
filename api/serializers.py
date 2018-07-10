from rest_framework import serializers

from api import models


class HourSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Hour
        fields = ('status', 'status_text', 'is_open', 'is_local_holiday')


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Photo
        fields = ('prefix', 'suffix', 'width', 'height')


class RestaurantSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = models.Restaurant
        fields = ('id', 'name', 'lat', 'lng', 'hour', 'website', 'photos')
