#!/usr/bin/python3
"""
This is the script for BaseModel Class.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ This class contains functionalities common to all
    other classes, from which they inherit.
    """

    def __init__(self, *args, **kwargs):
        """This func initializes the instance attributes of the
        BaseModel class.
        """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """This func returns the string representations
        of the objs
        """

        class_name = type(self).__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """This func updataes the pub instance attri 'updated_at'
        with the current datetime.
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ This func returns as dict containing all keys/values-
        pairs of the __dict__ instance.
        """

        class_name = type(self).__name__
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = class_name
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()

        return (my_dict)
