#!/usr/bin/python3
# Import modules and stuff here

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class Reviews
    Public class attributes:

        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """

    place_id = ""
    user_id = ""
    text = ""
