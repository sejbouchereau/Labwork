from abc import ABC
from log import log


class Car(ABC):

    steel_unit: int = 0
    rubber_unit: int = 0

    @log
    def __init__(self, steel_unit: int, rubber_unit: int):
        self.steel_unit: int = steel_unit
        self.rubber_unit: int = rubber_unit
