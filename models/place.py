#!/usr/bin/python3

""" For modules and import """

from models.base_model import BaseModel


class Place(BaseModel):
    # Place class
    city_id = str('')
    user_id = str('')
    name = str('')
    description = str('')
    number_rooms = int(0)
    number_bathrooms = int(0)
    max_guest = int(0)
    price_by_night = int(0)
    latitude = float(0.0)
    longitude = float(0.0)
    amenity_ids = []
