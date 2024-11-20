import tkinter as tk
from tkinter import messagebox
import random
import os

class GameMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Menu")
        
        # Load high score
        self.high_score = self.load_high_score()

        # Label for the game title
        self.label_title = tk.Label(root, text="Number Guessing Game", font=("Helvetica", 18))
        self.label_title.pack(pady=20)

        # Display high score
        self.label_high_score = tk.Label(root, text=f"High Score: {self.high_score if self.high_score is not None else 'No record yet'} attempts", font=("Helvetica", 14), fg="blue")
        self.label_high_score.pack(pady=5)

        # Difficulty selection buttons
        self.difficulty = tk.StringVar()
        self.difficulty.set("Medium")  # Default difficulty

        tk.Label(root, text="Select Difficulty:", font=("Helvetica", 14)).pack(pady=10)
        tk.Radiobutton(root, text="Easy (60 seconds)", variable=self.difficulty, value="Easy", font=("Helvetica", 12)).pack()
        tk.Radiobutton(root, text="Medium (30 seconds)", variable=self.difficulty, value="Medium", font=("Helvetica", 12)).pack()
        tk.Radiobutton(root, text="Hard (15 seconds)", variable=self.difficulty, value="Hard", font=("Helvetica", 12)).pack()

        # Start game button
        self.start_button = tk.Button(root, text="Start Game", command=self.start_game, font=("Helvetica", 12))
        self.start_button.pack(pady=10)

        # Exit button
        self.exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Helvetica", 12))
        self.exit_button.pack(pady=10)

    def load_high_score(self):
        """Load high score from file"""
        if os.path.exists("highscore.txt"):
            with open("highscore.txt", "r") as file:
                return int(file.read())
        return None  # Return None if no high score file exists

    def save_high_score(self, score):
        """Save new high score to file"""
        with open("highscore.txt", "w") as file:
            file.write(str(score))

    def update_high_score_label(self):
        """Update the high score label with the latest score"""
        self.high_score = self.load_high_score()
        self.label_high_score.config(text=f"High Score: {self.high_score if self.high_score is not None else 'No record yet'} attempts")

    def start_game(self):
        # Close the menu and open the game window
        self.root.withdraw()  # Hide the menu window
        difficulty = self.difficulty.get()
        time_limit = 60 if difficulty == "Easy" else 30 if difficulty == "Medium" else 15
        game_window = tk.Toplevel(self.root)
        NumberGuessingGame(game_window, time_limit, self.root, self.high_score, self.save_high_score, self.update_high_score_label)

class NumberGuessingGame:
    def __init__(self, root, time_limit, menu_root, high_score, save_high_score_callback, update_high_score_label_callback):
        # Initial setup for the main window
        self.root = root
        self.root.title("Number Guessing Game")
        self.menu_root = menu_root
        self.high_score = high_score
        self.save_high_score_callback = save_high_score_callback
        self.update_high_score_label_callback = update_high_score_label_callback
        self.time_left = time_limit  # Set time based on selected difficulty
        self.game_started = True  # Game is started now
        self.timer_running = True

        # Generate a random number between 1 and 100
        self.target_number = random.randint(1, 100)
        self.attempts = 0  # Counter for the number of attempts

        # Label for the game title
        self.label_title = tk.Label(root, text="Guess the Number (1-100)", font=("Helvetica", 16))
        self.label_title.pack(pady=10)

        # Label to display the number of attempts
        self.label_attempts = tk.Label(root, text="Attempts: 0", font=("Helvetica", 12))
        self.label_attempts.pack(pady=5)

        # Entry field for the user's guess
        self.entry_guess = tk.Entry(root, width=10, font=("Helvetica", 14))
        self.entry_guess.pack(pady=5)

        # Button to submit the user's guess
        self.button_guess = tk.Button(root, text="Guess", command=self.check_guess, font=("Helvetica", 12))
        self.button_guess.pack(pady=10)

        # Label to display the countdown timer
        self.label_timer = tk.Label(root, text=f"Time Left: {self.time_left} seconds", font=("Helvetica", 12), fg="green")
        self.label_timer.pack(pady=5)

        # Start the countdown timer
        self.start_timer()

    def start_timer(self):
        """Start the countdown timer and update it every second."""
        if self.time_left > 0 and self.timer_running:
            self.time_left -= 1  # Decrement the time
            self.label_timer.config(text=f"Time Left: {self.time_left} seconds")
            
            # Change the timer color to red when time is below 10 seconds
            if self.time_left <= 10:
                self.label_timer.config(fg="red")
                
            # Schedule the next countdown update after 1 second
            self.root.after(1000, self.start_timer)
        elif self.time_left == 0 and self.timer_running:
            # If time runs out, show a timeout message and reset the game
            messagebox.showinfo("Time's up!", "You've run out of time!")
            self.return_to_menu()

    def check_guess(self):
        """Check the user's guess and display appropriate messages"""
        try:
            # Get the user's guess and convert it to an integer
            guess = int(self.entry_guess.get())
            self.attempts += 1  # Increment the attempts counter
            self.label_attempts.config(text=f"Attempts: {self.attempts}")

            # Check if the number is within the range of 1 to 100
            if guess < 1 or guess > 100:
                messagebox.showwarning("Invalid input", "Please guess a number between 1 and 100.")
            elif guess < self.target_number:
                messagebox.showinfo("Hint", "Too low! Try again.")
            elif guess > self.target_number:
                messagebox.showinfo("Hint", "Too high! Try again.")
            else:
                # Correct guess
                messagebox.showinfo("Congratulations!", f"You guessed the number in {self.attempts} attempts!")

                # Check if it's a new high score
                if self.high_score is None or self.attempts < self.high_score:
                    messagebox.showinfo("New High Score!", f"New high score with {self.attempts} attempts!")
                    self.save_high_score_callback(self.attempts)

                self.return_to_menu()  # Return to menu after a correct guess
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid integer.")

    def return_to_menu(self):
        """Return to the game menu and reset the game"""
        self.root.destroy()  # Close the game window
        self.update_high_score_label_callback()  # Update the high score label in the menu
        self.menu_root.deiconify()  # Show the menu window again

if __name__ == "__main__":
    # Create and run the main menu window
    root = tk.Tk()
    game_menu = GameMenu(root)
    root.mainloop()
