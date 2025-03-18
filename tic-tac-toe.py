import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [""] * 9  

        # Create buttons for the grid
        self.buttons = []
        for i in range(9):
            button = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                              command=lambda i=i: self.on_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        # Reset button
        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.grid(row=3, column=1, pady=10)

    def on_click(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def reset(self):
        # Reset the board and buttons
        self.current_player = "X"
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")

# Create the main window
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
