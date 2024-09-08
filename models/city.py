#!/usr/bin/python3

""" For modules and import """

from models.base_model import BaseModel


class City(BaseModel):
    """City class
    inherites from BaseModel
    """

    state_id = ""
    name = ""
