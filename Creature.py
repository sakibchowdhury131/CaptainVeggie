# Author: Vedanth Sirimalla
# Date: 11/26/2023
# Description: The Creature class is a subclass of FieldInhabitant, it is a creature on the game field,
# defined by x and y coordinates.

from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
    def __init__(self, x, y, field_inhabitant):
        super().__init__(field_inhabitant)
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y