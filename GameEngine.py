import os
import random
from Veggie import Veggie
from captain import Captain
from Rabbit import Rabbit


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

        with open(veggie_file, 'r') as f:
            lines = f.readlines()
        
        field_size_height = int(lines[0].strip().split(',')[1])      ## This is the height of the field read from the veggie file
        field_size_width = int(lines[0].strip().split(',')[2])       ## This is the height of the field read from the veggie file

        ## initializing the field slots to None
        for height in range(field_size_height):
            row = []
            for width in range(field_size_width):
                row.append(None)
            self._field.append(row)


        ## The remaining lines in the files should be used to create new Veggie objects that are 
        # added to the List of possible vegetables
        for line in lines[1:]:
            data = line.strip().split(',')
            veggie_name = data[0]
            veggie_symbol = data[1]
            veggie_point = data[2]
            obj = Veggie(veggie_name, veggie_symbol, veggie_point)
            self._all_possible_vegetables.append(obj)


        ## The field 2D List should be populated with NUMBEROFVEGGIES number of new Veggie objects, 
        # located at random locations in the field

        counter = self.__NUMBEROFVEGGIES

        while counter > 0:
            location_h = random.randrange(0, field_size_height)
            location_w = random.randrange(0, field_size_width)


            # If a chosen random location is occupied by another Veggie object, repeatedly 
            # choose a new location until an empty location is found
            while self._field[location_h][location_w] != None:
                location_h = random.randrange(0, field_size_height)
                location_w = random.randrange(0, field_size_width)
            
            self._field[location_h][location_w] = random.choice(self._all_possible_vegetables)
            counter -=1

        '''
        ## use this code section to display the field distribution


        for i in range(field_size_height):
            for j in range(field_size_width):
                if self._field[i][j] == None:
                    print('0', end=' ')
                else:
                    print(self._field[i][j].getFieldInhabitant(), end=' ')
            print()

        '''


    def initCaptain(self):

        field_size_height = len(self._field)
        field_size_width = len(self._field[0])

        location_h = random.randrange(0, field_size_height)
        location_w = random.randrange(0, field_size_width)


        # If a chosen random location is occupied by other Veggie objects, repeatedly 
        # choose a new location until an empty location is found
        while self._field[location_h][location_w] != None:
            location_h = random.randrange(0, field_size_height)
            location_w = random.randrange(0, field_size_width)
        
        self._captain = captain(location_h, location_w)
        self._field[location_h][location_w] = self._captain

        '''
        ## use this code section to display the field distribution


        for i in range(field_size_height):
            for j in range(field_size_width):
                if self._field[i][j] == None:
                    print('0', end=' ')
                else:
                    print(self._field[i][j].getFieldInhabitant(), end=' ')
            print()

        '''


    def initRabbits(self):
        counter = self.__NUMBEROFRABBITS
        field_size_height = len(self._field)
        field_size_width = len(self._field[0])

        while counter > 0:
            location_h = random.randrange(0, field_size_height)
            location_w = random.randrange(0, field_size_width)


            # If a chosen random location is occupied by another object, repeatedly 
            # choose a new location until an empty location is found
            while self._field[location_h][location_w] != None:
                location_h = random.randrange(0, field_size_height)
                location_w = random.randrange(0, field_size_width)
            
            rabbit = Rabbit(location_h, location_w)
            self._field[location_h][location_w] = rabbit
            self._rabbits_in_the_field.append(rabbit)
            counter -= 1
            
        '''
        ## use this code section to display the field distribution

        
        for i in range(field_size_height):
            for j in range(field_size_width):
                if self._field[i][j] == None:
                    print('0', end=' ')
                else:
                    print(self._field[i][j].getFieldInhabitant(), end=' ')
            print()
        '''


    
    def initializeGame(self):
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()

        '''
        ## use this code section to display the field distribution
        field_size_height = len(self._field)
        field_size_width = len(self._field[0])
        
        for i in range(field_size_height):
            for j in range(field_size_width):
                if self._field[i][j] == None:
                    print('0', end=' ')
                else:
                    print(self._field[i][j].getFieldInhabitant(), end=' ')
            print()
        '''

    def remainingVeggies(self):
        count = 0
        for row in self._field:
            for item in row:
                if isinstance(item, Veggie):
                    count += 1
        return count

    def intro(self):
        print("Welcome to the Veggie Harvest Game!")
        print("The goal of the game is to harvest as many vegetables as you can while avoiding rabbits.")
        print("Here are the possible vegetables and their symbols:")
        for veggie in self._all_possible_vegetables:
            print(f"Symbol: {veggie.getSymbol()}, Name: {veggie.getName()}, Points: {veggie.getPointValue()}")
        print(f"Captain Veggie symbol: {self._captain.getSymbol()}")
        print("Rabbit symbol: R")
        print("Let the harvest begin!")

    def printField(self):
        for row in self._field:
            for item in row:
                if item is None:
                    print('0', end=' ')
                else:
                    print(item.getFieldInhabitant(), end=' ')
            print()

    def getScore(self):
        return self._score

    def moveRabbits(self):
        for rabbit in self._rabbits_in_the_field:
            rabbit.move(self._field)

    def moveCptVertical(self, movement):
        self._captain.moveVertical(movement, self._field, self._all_possible_vegetables, self._score)

    def moveCptHorizontal(self, movement):
        self._captain.moveHorizontal(movement, self._field, self._all_possible_vegetables, self._score)

    def moveCaptain(self):
        direction = input("Enter the direction to move the Captain (W for Up, S for Down, A for Left, D for Right): ").upper()
        if direction == 'W':
            self.moveCptVertical(-1)
        elif direction == 'S':
            self.moveCptVertical(1)
        elif direction == 'A':
            self.moveCptHorizontal(-1)
        elif direction == 'D':
            self.moveCptHorizontal(1)
        else:
            print("Invalid input. Please enter W, S, A, or D.")

    def gameOver(self):
        print("Game Over!")
        print("Vegetables harvested:")
        for veggie in self._captain.getVeggiesHarvested():
            print(f"{veggie.getName()} ({veggie.getSymbol()})")
        print(f"Your score: {self._score}")

    def highScore(self):
        pass



# For debugging
# engine = GameEngine()
# engine.initializeGame()
