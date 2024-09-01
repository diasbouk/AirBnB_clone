#!/usr/bin/python3

# import stuff
import json


class FileStorage:
    # File storage class
    __file_path = 'storage.json'
    __objects = {}

    def all(self):
        return (FileStorage.__objects)

    def new(self, obj):
        FileStorage.__objects[f"{obj["__class__"]}.{obj["id"]}"] = obj

    def save(self):
        with open(FileStorage.__file_path, 'a') as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                data = f.read()
                FileStorage.__objects = json.loads(data)
        except (ValueError, FileNotFoundError):
            pass
