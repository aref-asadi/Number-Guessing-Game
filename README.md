### Number Guessing Game - Multiplayer with High Score

This is a multiplayer number guessing game built using Python's `tkinter` library. It includes a game menu, multiplayer support, difficulty levels, a countdown timer, and a high score feature that tracks the best performance across games.

## Features

1. **Multiplayer Mode**: Two players take turns guessing the number.
2. **Difficulty Levels**: 
   - Easy (60 seconds)
   - Medium (30 seconds)
   - Hard (15 seconds)
3. **High Score Tracking**: The game records and displays the best performance (minimum total attempts) across all games.
4. **Countdown Timer**: Keeps the game engaging by adding a time limit based on the selected difficulty.
5. **Hints System**: Provides hints ("Too low!" or "Too high!") to guide players.
6. **Graphical User Interface (GUI)**: Built using `tkinter` for a user-friendly experience.

## Installation

### Prerequisites

Ensure you have Python installed on your system. This game uses the `tkinter` library, which comes pre-installed with Python.

### Clone the Repository

```
git clone https://github.com/aref-asadi/number-guessing-game.git
cd number-guessing-game
```

### Run the Game

Execute the following command in your terminal to start the game:

```
python number_guessing_game.py
```

## How to Play

1. **Launch the Game**: Run the script to open the game menu.
2. **Enter Player Names**: Input names for Player 1 and Player 2.
3. **Select Difficulty**: Choose a difficulty level to set the countdown timer.
4. **Start the Game**: Press "Start Game" to begin.
5. **Guess the Number**:
   - Players take turns guessing a number between 1 and 100.
   - The game provides hints after each guess.
6. **Win or Lose**:
   - If a player guesses the number correctly, the game ends, and the total attempts are recorded.
   - If the timer runs out, the game ends, and you can return to the menu.

## High Score Feature

- The game saves the high score (minimum total attempts across both players) to a `highscore.txt` file.
- If a new high score is achieved, it will be saved and displayed in the game menu.

## File Structure

```
.
├── number_guessing_game.py      # Main game file
├── highscore.txt                # File for storing high score (generated at runtime)
├── LICENSE                      # License file
└── README.md                    # Readme file
```

## Customization

- **High Score File**: The high score is saved in `highscore.txt`. You can change the file name or location by modifying the `save_high_score` and `load_high_score` methods.
- **Difficulty Settings**: Adjust the time limits for each difficulty in the `start_game` method.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch-name`).
3. Clone your fork (`git clone https://github.com/your-username/number-guessing-game.git`)
4. Chnage your directory (`cd number-guessing-game`)
5. Commit your changes (`git commit -m 'Add a new feature'`).
6. Push to the branch (`git push origin feature-branch-name`).
7. Open a pull request.

## License

This project is licensed under the GNU General Public License v3.0.