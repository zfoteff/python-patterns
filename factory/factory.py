"""Factory pattern implemented using a shape factory
"""

__author__ = "Zac Foteff"
__version__ = "v1.0.0"

from abc import ABC, abstractmethod
from bin.db_helper import DBHelper
from bin.logger import Logger

log = Logger("singleton")
db = DBHelper(db_collection="singleton")

class Shape(ABC):
    """Abstract Shape product that our factories will produce. Contains abstract functions that must be 
    overwritten
    """

    @abstractmethod
    def area(self, width: int | float, height: int | float) -> float:
        """NOTE: Product can also have a default implementation
        """
        pass

class ShapeFactory(ABC):
    
    @abstractmethod
    def factory_method(self, shape_type: str):
        """NOTE: Factory can also have a default implementation
        """
        pass

    def return_products(self):
        pass