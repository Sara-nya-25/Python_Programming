Fruit Loops 🍎🥨
A terminal-based adventure game where you navigate a hazardous grid, collect fruit, avoid lava, and manage explosives to reach the exit. Built as a modular Python package.

🚀 Getting Started
Prerequisites
Python 3.10 or higher (The project uses modern type hinting and structural pattern matching).

Installation
Clone or download this project folder.

Ensure your directory structure looks like this:

Plaintext
FruitLoopsProject/
├── main.py           # The game launcher
└── Fruit_loop/       # The source package
    ├── __init__.py
    ├── game.py       # Main game loop
    ├── grid.py       # Map and wall logic
    ├── player.py     # Movement logic
    └── pickups.py    # Item and trap logic
Running the Game
You can run the game from the root directory (FruitLoopsProject/) using either of these methods:

Method A: Using the Launcher (Recommended)

Bash
python main.py
Method B: Running as a Module

Bash
python -m Fruit_loop.game
🎮 How to Play
Controls
W / A / S / D: Move Up, Left, Down, or Right.

B: Place a Bomb (explodes in 3 moves).

I: View your current Inventory.

P: List the fruits you have collected.

Q / X: Quit the game.

Game Mechanics
The Floor is Lava: Every step costs 1 point and leaves a lava trail (~).

Lava Damage: Stepping back into existing lava costs 5 points.

Fruit Salad: Collecting fruit (O) grants 20 points.

Grace Period: After picking up an item, you get 5 steps of "Free Move" protection where no points are deducted for movement or hazards.

Traps (X): Stepping on a trap costs 10 points. Traps stay on the board!

Chests & Keys: Find a Key (K) to unlock a Chest (C) for a 100-point treasure.

Fertile Soil: Every 25 moves, a new fruit randomly sprouts on the map.

The Exit (E): Collect all 7 initial items to unlock the exit and win the game.

🛠️ Technical Details
Modular Structure
This project is organized as a formal Python package to demonstrate clean architecture:

Absolute Imports: Used throughout to ensure the package is portable.

Encapsulation: Game state (score, inventory, move counts) is managed within the play_game() function scope to avoid global variable conflicts.

Grid Logic: Walls are generated using for loops in grid.py to create contiguous obstacles without creating unreachable areas.

Development with PyCharm
To set up a Run Configuration:

Go to Edit Configurations.

Select Module Name instead of Script Path.

Enter Fruit_loop.game.

Set the Working Directory to the root project folder (the parent of Fruit_loop).

📝 Planned Improvements (Version 3 Tasks)
[ ] AI Enemies: Implement 1-3 enemies with pathfinding logic.

[ ] Jump Command: Implement J + WASD for two-step movement.

[ ] Shovel Item: Add a tool to destroy specific wall segments.

[ ] Trap Disarm: Add the T command to safely remove traps.

[ ] TDD: Implement unit tests for movement and scoring logic using pytest.