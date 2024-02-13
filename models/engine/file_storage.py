#!/usr/bin/python3


"""
Main file for our project instances info
"""


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
            FileStorage.__objects["{}.{}\".format(obj.to_dict()['__class__'], obj.id)] = obj

        def save(self):
            """
            serializes __objects to the JSON file (path: __file_path)
            """

        def reload(self):
            """
            deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
            otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
            """
