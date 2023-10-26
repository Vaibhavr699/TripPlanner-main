from django import template 
import random

register = template.Library()

@register.filter
def count_many(param):
    return param.all().count()

@register.simple_tag
def spot_exists(trip, spot_id):
    for spot in trip.spots.all():
        if spot.spot_id == spot_id:
            return True
    
    return False

@register.filter
def trip_image_url(trip):
    trip_spots = trip.spots.all()
    random_index = random.randint(0,len(trip_spots)-1)
    image_url = trip_spots[random_index].main_image.url
    return image_url