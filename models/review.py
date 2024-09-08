#!/usr/bin/python3

""" For modules and import """

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class
    inherites from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""
