# Fruit Loops 🍎🥨
A terminal-based adventure game where you navigate a hazardous grid, collect fruit, avoid lava, and manage explosives to reach the exit. Built as a modular Python package.

## 🚀 Getting Started
### Prerequisites
Python 3.10 or higher (The project uses modern type hinting and structural pattern matching).

## Installation
Clone or download this project folder.

Ensure your directory structure looks like this:

```text
Game/
├── main.py           # The game launcher
└── Fruit_loop/       # The source package
    ├── __init__.py
    ├── game.py       # Main game loop
    ├── grid.py       # Map and wall logic
    ├── player.py     # Movement logic
    └── pickups.py    # Item and trap logic
```
## Running the Game
You can run the game from the root directory (Game/) using either of these methods:
### Method A: Running as a Module
Bash
python -m Fruit_loop.game
### Method B: Using the Launcher (Recommended)
Bash
python main.py

## 🎮 How to Play
### Controls
### W / A / S / D: Move Up, Left, Down, or Right.
### Jump + W / A / S / D: Moves 2 tiles Up, Left, Down, or Right.
### 'O' - Fruits to pickup, 'T'- Traps, 'K'-Key to Chest, 'C'- Chest of treasure

**B: Place a Bomb (explodes in 3 moves).**

**H: View Game Instructions and Help.**

**P: List the fruits you have collected.**

**Q / X: Quit the game.**

## Game Mechanics

- **The Floor is Lava:** Every step costs 1 point and leaves a lava trail (~).

- **Lava Damage:** Stepping back into existing lava costs -5 points.

- **Fruits:** Collecting a fruit 'O' grants 20 points.

- **Grace Period:** After picking up an item, you get 5 steps of "Free Move" protection where no points are deducted for movement or hazards.

- **Traps (X):** Stepping on a trap costs 10 points. Traps stay on the board!

- **Bombs (b):** 💣 destroys walls and traps surrounding it, gets activated in 3 moves, player stuck in explosion looses -15 points.

- **Chests & Keys:** Find a Key (K) to unlock a Chest (C) for a 100-point treasure.

- **Fertile Soil:** Every 25 moves, a new fruit 'O' randomly sprouts on the map.

- **Wrong Command:** Every Wrong command or Wrong move like 'Bump on walls'/ 'Exit before all fruits picked' -2 points.

- **The Exit (E):** Collect all 7 initial items to unlock the exit and win the game.

## 🛠️ Technical Details
### Modular Structure: 
This project is organized as a formal Python package to demonstrate clean architecture:

**Absolute Imports:** Used throughout to ensure the package is portable.

**Encapsulation:** Game state (score, inventory, move counts) is managed within the play_game() function scope to avoid global variable conflicts.

**Grid Logic:** Walls are generated using for loops in grid.py to create contiguous obstacles without creating unreachable areas. This handles the coordinate system and boundary logic.

**Player class:** This encapsulates the player's physical state. By keeping movement validation ensures the player object "knows" its own physical limits.

**Pickups:** This acts as a database for game items. It maps symbols (like 'O' or 'K') to values and names, allowing to balance the game's economy (points) in one place.

**Game Logic:** The Game engine that connects everything. Managing the high-level score and inventory, Enforcing rules (like the Exit check or Bomb explosions) and handling state changes.

**Unit Test cases:** Unit testcases are used as part of TDD to test grid initialization, State resetting, Make walls, jump test, jump on wall(negative and positive), Exit logic.  

### 🚀 Benefits of this Structure

- **Scalability:** 
- **Easier Debugging**
- **Reusability**

## 📝 Planned Improvements (Version 3 Tasks)
[ ] AI Enemies: Implement 1-3 enemies with pathfinding logic.

[ ] Shovel Item: Add a tool to destroy specific wall segments.

[ ] Trap Disarm: Add the T command to safely remove traps.

## Run Configuration with PyCharm
- To set up a Run Configuration:

- Go to Edit Configurations.

- Select Module Name instead of Script Path.

- Enter Fruit_loop.game.

- Set the Working Directory to the root project folder (the parent of Fruit_loop).