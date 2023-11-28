# Author: Hari Kiran V G
# Date: Nov 28 2023
# Description: Captain Class

from Creature import Creature

class Captain(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, 'V')
        self._veggies_collected = []

    def add_veggie(self, veggie):
        self._veggies_collected.append(veggie)

    def get_veggies_collected(self):
        return self._veggies_collected
