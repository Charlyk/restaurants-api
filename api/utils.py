import json

from httplib2 import Http

from api import models

foursquare_url = 'https://api.foursquare.com/v2/venues/explore?ll={lat},{lng}&' \
                 'section=food&venuePhotos=1&oauth_token=NKRP0KY5ZDZIBMCU3TZS4BMP4ZMIQZBQPLBTCPXSIGPWFJ1L&v=20160629'
client = Http()


def get_foursquare_place(lat, lng):
    response, data = client.request(foursquare_url.format(lat=lat, lng=lng), method='GET')
    if response['status'] == '200':
        json_data = json.loads(data.decode())
        restaurant_groups = json_data.get('response').get('groups')
        for group in restaurant_groups:
            restaurants_json = group.get('items')
            for rest in restaurants_json:
                venue = rest.get('venue')
                hours = venue.get('hours')
                # Check if we have this hour saved to database
                if hours:
                    hour = models.Hour.objects.filter(status=hours.get('status')).first()
                    if not hour:
                        # if we don't we need to save it so we can use it in the future
                        hour = models.Hour(
                            status=rest['venue']['hours']['status'],
                            status_text=rest['venue']['hours']['richStatus']['text'],
                            is_open=rest['venue']['hours']['isOpen'] == 'true',
                            is_local_holiday=rest['venue']['hours']['isLocalHoliday'] == 'true'
                        )
                        hour.save()
                # we need initially to get place id from response and check if we have this restaurant
                place_id = venue.get('id')
                if not models.Restaurant.objects.filter(place_id=place_id).exists():
                    # parse restaurants and add them to the database
                    restaurant = models.Restaurant(
                        name=venue.get('name'),
                        lat=venue.get('location').get('lat'),
                        lng=venue.get('location').get('lng'),
                        hour=hour,
                        website=venue.get('url'),
                        place_id=place_id
                    )
                    restaurant.save()
                    # save restaurant photos
                    save_restaurant_photos(restaurant, venue.get('photos').get('groups'))
                else:
                    # if restaurant is already registered we need to only update working hours
                    restaurant = models.Restaurant.objects.filter(place_id=place_id).first()
                    restaurant.hour = hour
                    restaurant.save()


def save_restaurant_photos(restaurant, photo_groups):
    for group in photo_groups:
        items = group.get('items')
        for item in items:
            photo_id = item.get('id')
            if not models.Photo.objects.filter(photo_id=photo_id).exists():
                models.Photo(
                    photo_id=photo_id,
                    prefix=item.get('prefix'),
                    suffix=item.get('suffix'),
                    width=item.get('width'),
                    height=item.get('height'),
                    restaurant=restaurant
                ).save()
