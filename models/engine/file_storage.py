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
        FileStorage.__objects["{}.{}".format(obj.to_dict()['__class__'], obj.id)] = obj
        # FileStorage.__objects[obj.__class__.__name__.id] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        dict = {}
        for key in FileStorage.__objects:
            dict[key] = FileStorage.__objects[key]
            with open(FileStorage.__file_path, "w") as file:
                file.write(json.dumps(dict))

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        # try:
        #     with open(FileStorage.__file_path, "r") as file:
        #         # dict = json.loads(file.read())
        #     for key in dict:
        #          self.new(eval(dict[key]["__class__"])(**dict[key]))
        # except FileNotFoundError:
        #     pass
