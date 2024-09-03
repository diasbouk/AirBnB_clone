#!/usr/bin/python3

# import stuff
import json
from models.base_model import BaseModel


class FileStorage:
    # File storage class
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj

    def save(self):
        with open(FileStorage.__file_path, "w") as file:
            jason = {}
            for k, v in FileStorage.__objects.items():
                jason[k] = v.to_dict()
            json.dump(jason, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                jason = json.load(f)
                dict = {}
                for key, val in jason.items():
                    dict = val
                    FileStorage.__objects[key] = BaseModel(**dict)
        except (FileNotFoundError, ValueError):
            pass
