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

    def moveVertical(self, movement, field, veggies, score):
        new_x, new_y = self._x, self._y + movement
        self._move_logic(new_x, new_y, field, veggies, score)

    def moveHorizontal(self, movement, field, veggies, score):
        new_x, new_y = self._x + movement, self._y
        self._move_logic(new_x, new_y, field, veggies, score)

    def _move_logic(self, new_x, new_y, field, veggies, score):
        if 0 <= new_x < len(field) and 0 <= new_y < len(field[0]):
            if field[new_x][new_y] is None:
                field[self._x][self._y], field[new_x][new_y] = None, self
                self._x, self._y = new_x, new_y
            elif isinstance(field[new_x][new_y], Veggie):
                veggie = field[new_x][new_y]
                self.addVeggie(veggie)
                print(f"Delicious vegetable found: {veggie.getName()}! Score +{veggie.get_points()}")
                score += veggie.get_points()
                field[self._x][self._y], field[new_x][new_y] = None, self
                self._x, self._y = new_x, new_y
            elif isinstance(field[new_x][new_y], Rabbit):
                print("Oops! Don't step on the rabbits.")
        else:
            print("Invalid move. Captain cannot move outside the boundaries.")   

    # Other getter/setter functions for x and y
    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y
