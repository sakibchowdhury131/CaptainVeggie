from GameEngine import GameEngine

def main():
    game_engine = GameEngine()
    game_engine.initializeGame()
    game_engine.intro()

    remaining_vegetables = game_engine.remainingVeggies()

    while remaining_vegetables > 0:
        print(f"Remaining Vegetables: {remaining_vegetables}")
        print(f"Your Score: {game_engine.getScore()}")
        game_engine.printField()
        game_engine.moveRabbits()
        game_engine.moveCaptain()
        remaining_vegetables = game_engine.remainingVeggies()


    game_engine.gameOver()
    game_engine.highScore()

if __name__ == "__main__":
    main()