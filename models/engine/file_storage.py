#!/usr/bin/python3
"""This is the FileStorage module"""

import json
from models.base_model import BaseModel


class FileStorage():
    """The class FileStorage that serializes and deserializes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = f"{__class__.__name__}{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_s = {}
        for key, val in self.__objects.items():
            obj_s[key] = val.to_dict()
        with open(self.__file_path, 'w') as afile:
            afile.write(json.dumps(obj_s))
