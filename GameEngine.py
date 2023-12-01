import os


class GameEngine:

    def __init__(self):
        self.__NUMBEROFVEGGIES = 30
        self.__NUMBEROFRABBITS = 5
        self.__HIGHSCOREFILE = 'highscore.data'
        self._field = []
        self._rabbits_in_the_field = []
        self._captain = None
        self._all_possible_vegetables = []
        self._score = 0

    
    def initVeggies(self):
        veggie_file = input("Please enter the name of the vegetable point file: ")

        while not os.path.exists(veggie_file):
            veggie_file = input(f"{veggie_file} does not exist! Please enter the name of the vegetable point file: ")

