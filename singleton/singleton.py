__author__ = "Zac Foteff"
__version__ = "v1.0.0"

from bin.db_helper import DBHelper
from bin.logger import Logger

log = Logger("singleton")
db = DBHelper(db_collection="singleton")


class Singleton(object):
    """Singleton class object. Cannot be instantiated, can only be called to get the current state
    of the class object
    """

    __instance = None
    __objects = None

    def __init__(self):
        """Private constructor for Singleton objects


        Raises:
            RuntimeError: Runtime error if user tries to instantiate a object
        """
        raise RuntimeError("Call instance() instead")

    def __str__(cls) -> str:
        return f"{cls.__objects}"

    @classmethod
    def __persist(cls) -> bool:
        """TODO: Persist a Singleton object's data to the db so it can be retrieved on startup

        Returns:
            bool: True if object was persisted successfully, False otherwise
        """
        pass

    @classmethod
    def __restore(cls) -> bool:
        """TODO: Restore a Singleton object's data from the db on program start

        Returns:
            bool: True if object was persisted successfully, False otherwise
        """
        pass

    @classmethod
    def instance(cls):
        """Access the singleton instance. Method will create a new instance and its data
        container if none exists, it will return the class object otherwise

        Returns:
            Singleton: Singleton class object
        """
        if cls.__instance is None or cls.__objects is None:
            log("Creating new instance")
            cls.__instance = cls.__new__(cls)
            cls.__objects = dict()
        return cls.__instance

    @classmethod
    def append(cls, key: any = "", value: any = None):
        """Append a key-value pair to the Singleton object data

        Args:
            key (any, optional): Key to store in object data. Defaults to "".
            value (any, optional): Value to store in object data. Defaults to None.
        """
        if cls.__objects is None:
            log("[-] No object data exists for singleton instance")
            return

        if key not in cls.__objects.keys():
            #   Dont allow users to append new kv pair to objects if the key already exists
            cls.__objects[key] = value
            log(f"[+] Added new cell to the object data: [{key}, {value}]")

    @classmethod
    def get_objects(cls) -> dict:
        return cls.__objects
