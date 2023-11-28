# Author: Hari Kiran V G
# Date: Nov 28 2023
# Description: Rabbit Class

from Creature import Creature

class Rabbit(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, 'R')
