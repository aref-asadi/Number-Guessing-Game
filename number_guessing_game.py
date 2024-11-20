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
        self.label_title = tk.Label(root, text="Number Guessing Game - Multiplayer", font=("Helvetica", 18))
        self.label_title.pack(pady=20)

        # Entry fields for player names
        tk.Label(root, text="Player 1 Name:", font=("Helvetica", 14)).pack(pady=5)
        self.player1_name_entry = tk.Entry(root, font=("Helvetica", 12))
        self.player1_name_entry.pack(pady=5)

        tk.Label(root, text="Player 2 Name:", font=("Helvetica", 14)).pack(pady=5)
        self.player2_name_entry = tk.Entry(root, font=("Helvetica", 12))
        self.player2_name_entry.pack(pady=5)

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
        # Get player names
        player1_name = self.player1_name_entry.get()
        player2_name = self.player2_name_entry.get()

        # Validate player names
        if not player1_name or not player2_name:
            messagebox.showwarning("Invalid input", "Please enter names for both players.")
            return

        # Close the menu and open the game window
        self.root.withdraw()  # Hide the menu window
        difficulty = self.difficulty.get()
        time_limit = 60 if difficulty == "Easy" else 30 if difficulty == "Medium" else 15
        game_window = tk.Toplevel(self.root)
        NumberGuessingGame(game_window, time_limit, self.root, player1_name, player2_name, self.high_score, self.save_high_score, self.update_high_score_label)

class NumberGuessingGame:
    def __init__(self, root, time_limit, menu_root, player1_name, player2_name, high_score, save_high_score_callback, update_high_score_label_callback):
        self.root = root
        self.root.title("Number Guessing Game")
        self.menu_root = menu_root
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.players = [self.player1_name, self.player2_name]
        self.attempts = {self.player1_name: 0, self.player2_name: 0}
        self.current_player = self.player1_name
        self.high_score = high_score
        self.save_high_score_callback = save_high_score_callback
        self.update_high_score_label_callback = update_high_score_label_callback
        self.time_left = time_limit
        self.target_number = random.randint(1, 100)

        # Labels and entry field
        tk.Label(root, text="Guess the Number (1-100)", font=("Helvetica", 16)).pack(pady=10)
        self.label_current_player = tk.Label(root, text=f"Current Player: {self.current_player}", font=("Helvetica", 12))
        self.label_current_player.pack(pady=5)
        self.label_attempts = tk.Label(root, text=f"{self.current_player}'s Attempts: 0", font=("Helvetica", 12))
        self.label_attempts.pack(pady=5)
        self.entry_guess = tk.Entry(root, width=10, font=("Helvetica", 14))
        self.entry_guess.pack(pady=5)
        self.button_guess = tk.Button(root, text="Guess", command=self.check_guess, font=("Helvetica", 12))
        self.button_guess.pack(pady=10)
        self.label_timer = tk.Label(root, text=f"Time Left: {self.time_left} seconds", font=("Helvetica", 12), fg="green")
        self.label_timer.pack(pady=5)

        # Start timer
        self.start_timer()

    def start_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.label_timer.config(text=f"Time Left: {self.time_left} seconds")
            if self.time_left <= 10:
                self.label_timer.config(fg="red")
            self.root.after(1000, self.start_timer)
        else:
            messagebox.showinfo("Time's up!", "Time ran out!")
            self.return_to_menu()

    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
            self.attempts[self.current_player] += 1
            self.label_attempts.config(text=f"{self.current_player}'s Attempts: {self.attempts[self.current_player]}")
            if guess < 1 or guess > 100:
                messagebox.showwarning("Invalid input", "Guess a number between 1 and 100.")
            elif guess < self.target_number:
                messagebox.showinfo("Hint", "Too low!")
            elif guess > self.target_number:
                messagebox.showinfo("Hint", "Too high!")
            else:
                messagebox.showinfo("Congratulations!", f"{self.current_player} guessed it in {self.attempts[self.current_player]} attempts!")
                total_attempts = self.attempts[self.player1_name] + self.attempts[self.player2_name]
                if self.high_score is None or total_attempts < self.high_score:
                    messagebox.showinfo("New High Score!", f"New high score with {total_attempts} total attempts!")
                    self.save_high_score_callback(total_attempts)
                self.return_to_menu()
                return
            self.current_player = self.player2_name if self.current_player == self.player1_name else self.player1_name
            self.label_current_player.config(text=f"Current Player: {self.current_player}")
            self.label_attempts.config(text=f"{self.current_player}'s Attempts: {self.attempts[self.current_player]}")
            self.entry_guess.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid integer.")

    def return_to_menu(self):
        self.root.destroy()
        self.update_high_score_label_callback()
        self.menu_root.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    game_menu = GameMenu(root)
    root.mainloop()
