#!/usr/bin/python3
"""
This moddule defines the FileStorage class.
"""

import os
import json
import datetime


class FileStorage:
    """This class stores and retrieve data via
    serializationa-deserializaton using  JSON objs.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This func returns hthe dictionary __objects.
        """

        return (FileStorage.__objects)

    def new(self, obj):
        """This func. sets in __objects the
        obj with key <obj class name>.id.
        """

        class_name = type(obj).__name__
        key = ("{}.{}".format(class_name, obj.id))
        FileStorage.__objects[key] = obj

    def save(self):
        """This func. serializes __objects to
        the JSON file (path: __file_path).
        """

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """This func. deserializes/relods the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise,
        take no action. If the file doesn't exist, no exception is raised.
        """

        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            dict_obj = json.load(f)
            dict_obj = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = dict_obj
