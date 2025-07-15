import tkinter as tk
from tkinter import messagebox

# Initialize window
root = tk.Tk()
root.title("Tic Tac Toe (XO)")

# Global variables
current_player = "X"
board = [""] * 9

# Button click handler
def on_click(index):
    global current_player

    if board[index] == "" and not check_winner():
        board[index] = current_player
        buttons[index].config(text=current_player)

        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        elif "" not in board:
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Check for winner
def check_winner():
    win_combinations = [
        (0,1,2), (3,4,5), (6,7,8),  # Rows
        (0,3,6), (1,4,7), (2,5,8),  # Columns
        (0,4,8), (2,4,6)            # Diagonals
    ]

    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    return None

# Reset the game
def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for btn in buttons:
        btn.config(text="")

# Create buttons
buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=('Helvetica', 24), width=5, height=2, command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Run the GUI loop
root.mainloop()
