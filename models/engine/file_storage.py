#!/usr/bin/python3

"""
    Module for storage and handling data
    json: Serializing and deserializing objects and instances
    BaseModel: To recreate instances from file.json
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
            FileStorage class
            Controls storage for our
            instances
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """ Class constructor """
        pass

    def all(self):
        """ Returns the __objects dict """
        return FileStorage.__objects

    def new(self, obj):
        """ Creates new objects and insert it
                to the __objects dict """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj

    def save(self):
        """ Saves all objects to file.json """
        with open(FileStorage.__file_path, "w") as file:
            jason = {}
            for k, v in FileStorage.__objects.items():
                jason[k] = v.to_dict()
            json.dump(jason, file)

    def reload(self):
        """  Reloads the instances from the file.json """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                jason = json.load(f)
                dict = {}
                for key, val in jason.items():
                    dict = val
                    FileStorage.__objects[key] = BaseModel(**dict)
        except (FileNotFoundError, ValueError):
            pass
