# Number Guessing Game

An enhanced number guessing game built with Python and `tkinter`, now featuring difficulty levels, a countdown timer, and a game menu! In this game, players can select their preferred difficulty level, which affects the time limit for guessing the number between 1 and 100. 

## Features
- **Difficulty Levels**: Players can choose from Easy (60 seconds), Medium (30 seconds), or Hard (15 seconds) before starting the game.
- **Countdown Timer**: A countdown timer provides urgency, turning red when fewer than 10 seconds are left.
- **Game Menu**: A main menu allows players to choose the difficulty level, start the game, or exit.
- **Feedback System**: Gives hints on whether each guess is too high or too low, and tracks the number of attempts.
- **Attempt Counter**: Tracks the number of attempts, motivating players to improve with each game.

## Project Structure
- `GameMenu` Class: Handles the main menu where users select difficulty levels and start or exit the game.
  - `__init__(self, root)`: Initializes menu options and difficulty level selection.
  - `start_game(self)`: Starts a new game with the selected difficulty and time limit.
- `NumberGuessingGame` Class: Manages the main gameplay, timer, and feedback.
  - `__init__(self, root, time_limit, menu_root)`: Sets up the game window, initializes the timer, and tracks attempts.
  - `start_timer(self)`: Starts the countdown timer, updating every second.
  - `check_guess(self)`: Checks the user's guess, provides hints, and congratulates the player upon a correct guess.
  - `return_to_menu(self)`: Closes the game window and returns to the main menu.

## Prerequisites
- **Python 3.x** installed on your system
- **tkinter** library (typically included with Python installations)

## How to Install and Run
1. Clone the project repository:
   ```bash
   git clone https://github.com/aref-asadi/number_guessing_game.git
   cd number_guessing_game
   ```
2. Run the game with:
   ```bash
   python guess_number_gui.py
   ```

## How to Play
1. Select a difficulty level from the main menu:
   - **Easy**: 60 seconds
   - **Medium**: 30 seconds
   - **Hard**: 15 seconds
2. Click **Start Game** to begin.
3. Enter a number between 1 and 100 in the input field.
4. Click the **Guess** button to submit your guess. The game provides feedback on whether your guess is too high or too low.
5. If the timer runs out, a message will appear, and you can return to the menu to start a new game.
6. If you guess correctly, the game congratulates you and takes you back to the menu.

## Example Gameplay
- **User selects Medium difficulty** (30 seconds).
- **User Input**: 50
- **Feedback**: "Too high! Try again."
- **User Input**: 25
- **Feedback**: "Too low! Try again."
- **User Input**: 37
- **Feedback**: "Congratulations! You guessed the number in 3 attempts!"

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch with your feature or bug fix.
3. Commit your changes and push the branch.
4. Submit a pull request detailing your changes.

## License
This project is licensed under the GNU General Public License v3.0.