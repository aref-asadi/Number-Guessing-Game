import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        # Initial setup for the main window
        self.root = root
        self.root.title("Number Guessing Game")

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
            # Check if the guess is lower than the target number
            elif guess < self.target_number:
                messagebox.showinfo("Hint", "Too low! Try again.")
            # Check if the guess is higher than the target number
            elif guess > self.target_number:
                messagebox.showinfo("Hint", "Too high! Try again.")
            # If the guess is correct
            else:
                messagebox.showinfo("Congratulations!", f"You guessed the number in {self.attempts} attempts!")
                self.reset_game()  # Restart the game after a correct guess
        except ValueError:
            # Show an error message if the input is not a valid integer
            messagebox.showerror("Invalid input", "Please enter a valid integer.")

    def reset_game(self):
        """Reset the game for a new round"""
        self.target_number = random.randint(1, 100)  # Generate a new random number
        self.attempts = 0  # Reset the attempt counter
        self.label_attempts.config(text="Attempts: 0")  # Update the attempts display
        self.entry_guess.delete(0, tk.END)  # Clear the entry field

if __name__ == "__main__":
    # Create and run the game window
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
