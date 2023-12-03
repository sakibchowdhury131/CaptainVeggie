# Author: Hari Kiran V G
# Date: Nov 28 2023
# Description: Rabbit Class

# Rabbit.py

from Creature import Creature

class Rabbit(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "R")

    # Getter and setter functions for x and y
    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

