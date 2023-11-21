__author__ = "Zac Foteff"
__version__ = "v1.0.0"

from bin.logger import Logger

log = Logger("strategy")

class Context():
    __strategy = None

    def __init__(self, strategy: Strategy = None) -> None:
        self.__strategy = strategy

    @setter.property
    def strategy(self, strategy: Strategy) -> None:
        self.__strategy = strategy

    
class Strategy():
    pass
