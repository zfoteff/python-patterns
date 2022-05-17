__version__ = "1.0.0"
__author__ = "Zac Foteff"

from pymongo import MongoClient

from bin.logger import Logger
from bin.constants import *


class DBHelper:
    """Database helper class"""

    def __init__(
        self, db_name: str = "patterns", db_collection: str = "collection"
    ) -> None:
        self.__db_name = db_name
        self.__db_collection_name = db_collection
        self.__db_client = MongoClient(DEV_MONGO_URL)
        self.__db = self.__db_client.get_database(self.__db_name)
        self.__db_collection = self.__db.get_collection(self.__db_collection_name)

    @property
    def db_name(self) -> str:
        return self.__db_name

    @property
    def collection_name(self) -> str:
        return self.__db_collection_name

    @property
    def collection(self) -> any:
        return self.__db_collection
