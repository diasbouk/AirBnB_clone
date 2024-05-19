#!/usr/bin/python3


"""
Main file for our project instances info
"""

import json

# from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.city import City
# from models.place import Place
# from models.amenity import Amenity
# from models.review import Review


class FileStorage:
    """
    Class representing our storage
    Operations :
        Dict ==> JSON file
        JSON file ==> Dict
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id

        Args:
            obj:

        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        dict = {}
        with open(FileStorage.__file_path, "w+") as file:
            dict = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, "r") as file:
                dict = json.loads(file.read())
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
