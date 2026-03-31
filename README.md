# CaptainVeggie

A terminal-based Python game where the player controls Captain Veggie to collect vegetables before rabbits eat them all. This is a coursework/academic project demonstrating object-oriented design in Python.

## Features

- Grid-based playing field populated with vegetables and rabbits
- Player-controlled Captain Veggie character
- Randomly moving rabbits that consume vegetables
- Score tracking and high-score persistence (`highscore.data`)
- Game over screen and leaderboard

## Tech Stack

- Python 3 (standard library only)

## Project Structure

| File | Description |
|---|---|
| `main.py` | Entry point: game loop logic |
| `GameEngine.py` | Core game engine: field initialization, movement, scoring |
| `captain.py` | Captain Veggie player character class |
| `Creature.py` | Base creature class |
| `FieldInhabitant.py` | Base class for all field entities |
| `Rabbit.py` | Rabbit entity class |
| `Veggie.py` | Vegetable entity class |
| `highscore.data` | Persistent high-score storage |

## Requirements

- Python 3.6+

## Usage

```bash
python main.py
```

Follow the on-screen prompts to move Captain Veggie using keyboard input.

## License

MIT
