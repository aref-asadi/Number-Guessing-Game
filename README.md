# Number Guessing Game

A simple, interactive number guessing game built with Python and `tkinter`. This game challenges players to guess a randomly generated number between 1 and 100, providing feedback after each guess. A fun and engaging way to practice programming with graphical interfaces and input validation!

## Features
- **Random Number Generation**: A new random number between 1 and 100 is generated for each round, ensuring a unique game experience.
- **User Feedback**: Provides hints on whether each guess is too high or too low, guiding the player closer to the answer.
- **Attempt Counter**: Tracks the number of attempts, adding an extra layer of challenge for players to guess in as few tries as possible.
- **Input Validation**: Handles invalid inputs gracefully, ensuring the game only accepts integer guesses within the correct range.

## Project Structure
- `NumberGuessingGame` Class: Contains the main game logic and GUI components.
  - `__init__(self, root)`: Sets up the main window with labels, input fields, and buttons.
  - `check_guess(self)`: Handles the user's input, checks it against the target number, and provides feedback.
  - `reset_game(self)`: Resets the game state to start a new round, generating a fresh random number and resetting the attempt counter.

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
   python number_guessing_game.py
   ```

## How to Play
1. Enter a number between 1 and 100 in the input field.
2. Click the **Guess** button to submit your guess.
3. The game will provide feedback on whether your guess is too high, too low, or correct.
4. Continue guessing based on the feedback until you find the correct number.
5. When you guess correctly, a congratulatory message appears, and the game automatically resets for a new round.

## Example Gameplay
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