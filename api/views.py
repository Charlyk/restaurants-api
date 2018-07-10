from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from api import models, utils, serializers


@api_view(http_method_names=['get'])
def get_nearby_places(request):
    """
    Get request for obtaining nearby restaurants based on latitude and longitude.
    :param request: with GET parameters [lat, lng, radius]
    :return: a list of places
    """
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    radius = request.GET.get('radius')
    if not lat or not lng or not radius:
        return Response({'details': 'Not all parameters specified'}, status.HTTP_400_BAD_REQUEST)

    user_location = (float(lat), float(lng))
    # get places from foursquare and add them to database if needed
    utils.get_foursquare_place(lat, lng)
    restaurants = list(filter(lambda restaurant: restaurant.is_in_range(user_location, int(radius)),
                              models.Restaurant.objects.all()))
    serializer = serializers.RestaurantSerializer(restaurants, many=True, context={'request': request})
    return Response(serializer.data, status.HTTP_200_OK)
