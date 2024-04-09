import tkinter as tk
import random

class GuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Number Guessing Game")
        self.geometry("500x450")
        self.resizable(False, False)
        
        self.configure(background='lightblue')  # Setting initial background color
        
        self.secret_number = random.randint(1, 50)
        self.attempts = 0
        
        # Changing appearance of the label
        label_font = ("Arial", 14, "bold")
        self.label = tk.Label(self, text="Guess a number between 1 and 50:", font=label_font)
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(self)
        self.entry.pack(pady=8)
        
        # Changing appearance of the buttons
        button_font = ("Arial", 12, "bold")
        self.guess_button = tk.Button(self, text="Guess the number", command=self.check_guess, bg='blue', fg='white', padx=20, pady=10, bd=4, relief=tk.RAISED, font=button_font)
        self.guess_button.pack(pady=10, padx=10, ipadx=10, ipady=5)
        
        self.reset_button = tk.Button(self, text="Reset", command=self.reset_game, bg='orange', fg='white', padx=15, pady=10, bd=4, relief=tk.RAISED, font=button_font)
        self.reset_button.pack(pady=8, padx=10, ipadx=10, ipady=5)
        
    def check_guess(self):
        guess = self.entry.get()
        if guess.isdigit():
            guess = int(guess)
            self.attempts += 1
            if guess < self.secret_number:
                self.display_hint("Too low! Try again for some another guess", 'lightcoral')
            elif guess > self.secret_number:
                self.display_hint("Too high! Try again for some another guess", 'lightcoral')
            else:
                self.display_hint(f" The number was {self.secret_number}.", 'lightgreen')
                self.display_congratulations()
                self.reset_game()
        else:
            self.display_error("Error", "Please enter a valid number!")
        
    def reset_game(self):
        self.secret_number = random.randint(1, 50)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.configure(background='lightblue')  # Reset background color
        
    def display_hint(self, hint, color):
        self.label.config(text=hint)
        self.configure(background=color)  # Change background color
        
    def display_error(self, title, message):
        error_window = tk.Toplevel(self)
        error_window.title(title)
        error_window.geometry("300x100")
        error_window.resizable(False, False)
        error_window.configure(background='lightcoral')
        
        tk.Label(error_window, text=message, font=("Arial", 12), bg='lightcoral').pack(pady=10)
        tk.Button(error_window, text="OK", command=error_window.destroy, font=("Arial", 12)).pack()
    
    def display_congratulations(self):
        congrats_window = tk.Toplevel(self)
        congrats_window.title("Congratulations")
        congrats_window.geometry("400x110")
        congrats_window.resizable(False, False)
        congrats_window.configure(background='lightgreen')
        
        tk.Label(congrats_window, text="You guessed it right!", font=("Arial", 12), bg='lightgreen').pack(pady=5)
        tk.Label(congrats_window, text=f"The Number of attempts you took to guess: {self.attempts}", font=("Arial", 12), bg='lightgreen').pack(pady=5)
        tk.Button(congrats_window, text="OK", command=congrats_window.destroy, font=("Arial", 12)).pack()

if __name__ == "__main__":
    game = GuessingGame()
    game.mainloop()
