import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")
        self.master.geometry("450x450")
        self.master.resizable(False, False)

        self.board = [[tk.StringVar() for _ in range(9)] for _ in range(9)]

        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            for j in range(9):
                row_block = i // 3
                col_block = j // 3
                if (row_block + col_block) % 2 == 0:
                    entry_bg = '#f0f0f0'  # Light gray
                else:
                    entry_bg = '#ffffff'  # White
                entry = tk.Entry(self.master, width=2, font=('Arial', 18), textvariable=self.board[i][j], justify='center', bg=entry_bg)
                entry.grid(row=i, column=j, padx=0, pady=0, ipadx=5, ipady=5)
                entry.bind('<KeyPress>', lambda event, row=i, col=j: self.validate_input(event, row, col))
        
        solve_button = tk.Button(self.master, text="Solve", command=self.solve, bg='#4caf50', fg='white')  # Green
        solve_button.grid(row=9, column=3, columnspan=3, pady=5, sticky="ew")

        reset_button = tk.Button(self.master, text="Reset", command=self.reset, bg='#f44336', fg='white')  # Red
        reset_button.grid(row=9, column=6, columnspan=3, pady=5, sticky="ew")

        # Align buttons to center
        for i in range(10):
            self.master.grid_columnconfigure(i, weight=1)
        self.master.grid_rowconfigure(9, weight=1)

    def validate_input(self, event, row, col):
        if not event.char.isdigit():
            self.board[row][col].set('')
            messagebox.showerror("Invalid Input", "Only numbers are allowed in Sudoku grid.")

    def solve(self):
        self.get_input()
        if self.solve_sudoku():
            self.display_solution()
        else:
            messagebox.showinfo("Sudoku Solver", "No solution exists!")

    def get_input(self):
        for i in range(9):
            for j in range(9):
                value = self.board[i][j].get()
                if value and value.isdigit():
                    self.board[i][j].set(value)
                else:
                    self.board[i][j].set("")

    def solve_sudoku(self):
        empty = self.find_empty()
        if not empty:
            return True
        row, col = empty

        for num in range(1, 10):
            if self.is_valid_move(row, col, str(num)):
                self.board[row][col].set(str(num))
                if self.solve_sudoku():
                    return True
                self.board[row][col].set("")
        return False

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if not self.board[i][j].get():
                    return (i, j)
        return None

    def is_valid_move(self, row, col, num):
        for i in range(9):
            if self.board[i][col].get() == num or self.board[row][i].get() == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j].get() == num:
                    return False
        return True

    def display_solution(self):
        pass

    def reset(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j].set("")

def main():
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()

if __name__ == "__main__":
    main()
