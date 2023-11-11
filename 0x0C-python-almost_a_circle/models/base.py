#!/usr/bin/python3
"""Module containing the Base class for managing id attribute."""
import json


class Base:
    """Base class for managing id attribute."""

    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor.

        Args:
            id (int): If provided, assigns the public instance attribute id
                      with this value.
                      If not provided, increments __nb_objects and assigns
                      the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        # Sort the list of dictionaries based on the 'id' key
        sorted_list = sorted(list_dictionaries, key=lambda x: x.get('id', 0))
        return json.dumps(sorted_list)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries represented by json_string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []

        # Get the class name (assuming all elements in list_objs
        # are of the same class)
        class_name = cls.__name__

        # Create the filename
        filename = "{}.json".format(class_name)

        # Convert instances to a list of dictionaries
        dict_list = [obj.to_dictionary() for obj in list_objs]

        # Convert the list of dictionaries to a JSON string
        json_string = cls.to_json_string(dict_list)

        # Write the JSON string to the file
        with open(filename, 'w') as file:
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)  # A Rectangle with default values
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)  # Create a Square with default values
        else:
            dummy_instance = cls()  # Generic instance with default values

        dummy_instance.update(**dictionary)  # Update with real values
        return dummy_instance
