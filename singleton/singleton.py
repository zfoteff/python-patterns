__author__ = "Zac Foteff"
__version__ = "v1.0.0"

from bin.db_helper import DBHelper
from bin.logger import Logger

db = DBHelper(db_collection="singleton")

class Singleton(object):
    __objects = None

    @staticmethod
    def __persist(self) -> bool:
        pass

    @staticmethod
    def __restore(self) -> bool:
        pass

    @staticmethod
    def __get_instance(self):
        if Singleton.__objects is None:
            __objects = dict()
            self.__persist()

    def __call__(self, *args: any, **kwds: any) -> any:
        pass