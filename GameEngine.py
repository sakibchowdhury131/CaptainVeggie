import os
import random
import pickle
from Veggie import Veggie
from Captain import Captain
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
            veggie_point = int(data[2])
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
        
        self._captain = Captain(location_h, location_w)
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
            # Save the current location of the rabbit
            current_location = (rabbit.get_x(), rabbit.get_y())

            # Attempt to move the rabbit in a random direction
            new_location = self.getRandomMove(current_location)

            # Check if the new location is within the field boundaries
            if self.isWithinBoundaries(new_location):
                new_x, new_y = new_location

                # Check if the new location is occupied by another rabbit or captain
                if not self.isOccupied(new_location):
                    # Update the field with the new location
                    self._field[current_location[0]][current_location[1]] = None
                    self._field[new_x][new_y] = rabbit

                    # Update the rabbit's location
                    rabbit.set_x(new_x)
                    rabbit.set_y(new_y)
                else:
                    # Rabbit forfeits its move if the new location is occupied
                    pass

    def getRandomMove(self, current_location):
        x, y = current_location
        # Generate random move (up, down, left, right, diagonal, or no move)
        new_x = x + random.choice([-1, 0, 1])
        new_y = y + random.choice([-1, 0, 1])

        return new_x, new_y

    def isWithinBoundaries(self, location):
        x, y = location
        return 0 <= x < len(self._field) and 0 <= y < len(self._field[0])

    def isOccupied(self, location):
        x, y = location
        return self._field[x][y] is not None
    


    def moveCptVertical(self, vertical_movement):
        captain = self._captain
        current_location = (captain.get_x(), captain.get_y())
        new_location = (current_location[0] + vertical_movement, current_location[1])

        if self.isWithinBoundaries(new_location):
            if not self.isOccupied(new_location):
                # Move Captain to an empty slot
                self.moveCaptainInField(current_location, new_location)
            elif isinstance(self._field[new_location[0]][new_location[1]], Veggie):
                # Move Captain to a space occupied by a Veggie
                self.collectVeggie(current_location, new_location)
            elif isinstance(self._field[new_location[0]][new_location[1]], Rabbit):
                # Inform the player not to step on rabbits
                print("Oops! You should not step on the rabbits. Try a different move.")
        else:
            print("Oops! Movement would go beyond field boundaries.")

    def moveCaptainInField(self, current_location, new_location):
        # Update Captain's member variables
        self._captain.set_x(new_location[0])
        self._captain.set_y(new_location[1])

        # Update field
        self._field[current_location[0]][current_location[1]] = None
        self._field[new_location[0]][new_location[1]] = self._captain

    def collectVeggie(self, current_location, new_location):
        # Update Captain's member variables
        self._captain.set_x(new_location[0])
        self._captain.set_y(new_location[1])

        # Collect Veggie details
        veggie = self._field[new_location[0]][new_location[1]]
        veggie_name = veggie.get_name()
        veggie_point_value = veggie.get_points()

        # Output message
        print(f"Delicious vegetable found: {veggie_name}! You earned {veggie_point_value} points.")

        # Add Veggie to Captain's List of Veggies
        self._captain.addVeggie(veggie)

        # Increment the score
        self._score += veggie_point_value

        # Update field
        self._field[current_location[0]][current_location[1]] = None
        self._field[new_location[0]][new_location[1]] = self._captain

    def moveCptHorizontal(self, horizontal_movement):
        captain = self._captain
        current_location = (captain.get_x(), captain.get_y())
        new_location = (current_location[0], current_location[1] + horizontal_movement)

        if self.isWithinBoundaries(new_location):
            if not self.isOccupied(new_location):
                # Move Captain to an empty slot
                self.moveCaptainInField(current_location, new_location)
            elif isinstance(self._field[new_location[0]][new_location[1]], Veggie):
                # Move Captain to a space occupied by a Veggie
                self.collectVeggie(current_location, new_location)
            elif isinstance(self._field[new_location[0]][new_location[1]], Rabbit):
                # Inform the player not to step on rabbits
                print("Oops! You should not step on the rabbits. Try a different move.")
        else:
            print("Oops! Movement would go beyond field boundaries.")


    def moveCaptain(self):
        direction = input("Enter the direction to move the Captain (W/A/S/D): ").lower()

        if direction == 'w':
            self.moveCptVertical(-1)  # Move up
        elif direction == 's':
            self.moveCptVertical(1)   # Move down
        elif direction == 'a':
            self.moveCptHorizontal(-1)  # Move left
        elif direction == 'd':
            self.moveCptHorizontal(1)   # Move right
        else:
            print("Invalid input. Please enter W, A, S, or D.")

    
    def gameOver(self):
        print("Game Over!")
        
        # Output harvested vegetables
        veggies_collected = self._captain.get_veggies_collected()
        if not veggies_collected:
            print("You didn't harvest any vegetables.")
        else:
            print("You harvested the following vegetables:")
            for veggie in veggies_collected:
                print(f"- {veggie.get_name()}")

        # Output player's score
        print(f"Your final score is: {self._score}")


    def highScore(self):
        high_scores = []

        # Check if the highscore.data file exists
        if os.path.exists(self.__HIGHSCOREFILE):
            try:
                # Open the file for binary reading
                with open(self.__HIGHSCOREFILE, 'rb') as file:
                    # Unpickle the file into the List of high scores
                    high_scores = pickle.load(file)
            except Exception as e:
                print(f"Error reading high scores: {e}")

        # Prompt the user for their initials and extract the first 3 characters
        player_initials = input("Enter your initials: ")[:3]

        # Create a Tuple with the player’s initials and score
        player_score = (player_initials, self._score)

        if not high_scores:
            # If there are no high scores yet recorded, add the Tuple to the List
            high_scores.append(player_score)
        else:
            # Add the Tuple to the correct position in the List to maintain descending order
            index_to_insert = 0
            for index, (initials, score) in enumerate(high_scores):
                if self._score > score:
                    index_to_insert = index
                    break
                else:
                    index_to_insert = index + 1

            high_scores.insert(index_to_insert, player_score)

        # Output all of the high scores
        print("High Scores:")
        for rank, (initials, score) in enumerate(high_scores, start=1):
            print(f"{rank}. {initials}: {score}")

        try:
            # Open the highscore.data file for binary writing
            with open(self.__HIGHSCOREFILE, 'wb') as file:
                # Pickle the List of high scores to the file
                pickle.dump(high_scores, file)
        except Exception as e:
            print(f"Error writing high scores: {e}")


    # def moveCptVertical(self, movement):
    #     self._captain.moveVertical(movement, self._field, self._all_possible_vegetables, self._score)

    # def moveCptHorizontal(self, movement):
    #     self._captain.moveHorizontal(movement, self._field, self._all_possible_vegetables, self._score)

    # def moveCaptain(self):
    #     direction = input("Enter the direction to move the Captain (W for Up, S for Down, A for Left, D for Right): ").upper()
    #     if direction == 'W':
    #         self.moveCptVertical(-1)
    #     elif direction == 'S':
    #         self.moveCptVertical(1)
    #     elif direction == 'A':
    #         self.moveCptHorizontal(-1)
    #     elif direction == 'D':
    #         self.moveCptHorizontal(1)
    #     else:
    #         print("Invalid input. Please enter W, S, A, or D.")

    # def gameOver(self):
    #     print("Game Over!")
    #     print("Vegetables harvested:")
    #     for veggie in self._captain.getVeggiesHarvested():
    #         print(f"{veggie.getName()} ({veggie.getSymbol()})")
    #     print(f"Your score: {self._score}")

    # def highScore(self):
    #     pass



# For debugging
engine = GameEngine()
engine.initializeGame()
engine.printField()
print()
print()
engine.moveRabbits()
engine.printField()
print()
print()
engine.moveCaptain()
engine.printField()
engine.gameOver()
engine.highScore()
