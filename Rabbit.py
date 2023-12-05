# Author: Hari Kiran V G
# Date: Nov 28 2023
# Description: Rabbit Class

# Rabbit.py

from Creature import Creature

class Rabbit(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "R")

    def move(self, field):
        new_x, new_y = self._generate_random_move()

        if 0 <= new_x < len(field) and 0 <= new_y < len(field[0]):
            if field[new_x][new_y] is None:
                field[self._x][self._y], field[new_x][new_y] = None, self
                self._x, self._y = new_x, new_y
            elif isinstance(field[new_x][new_y], Veggie):
                # Handle logic when moving onto a Veggie
                pass
            elif isinstance(field[new_x][new_y], Captain):
                # Handle logic when moving onto a Captain
                pass

    def _generate_random_move(self):
        movement = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)])
        new_x, new_y = self._x + movement[0], self._y + movement[1]
        return new_x, new_y

    # Getter and setter functions for x and y
    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

