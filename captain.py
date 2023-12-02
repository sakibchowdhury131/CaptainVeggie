# Author: Hari Kiran V G
# Date: Nov 28 2023
# Description: Captain Class


from Creature import Creature

class Captain(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "V")
        self._veggies_collected = []

    def addVeggie(self, veggie):
        self._veggies_collected.append(veggie)

    def get_veggies_collected(self):
        return self._veggies_collected

    def set_veggies_collected(self, veggies_collected):
        self._veggies_collected = veggies_collected

    # Other getter/setter functions for x and y
    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y
