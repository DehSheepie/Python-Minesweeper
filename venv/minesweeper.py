from tkinter import *
from game import Game

size = 5
mines = 3


def start_game(size, mines):
    board = Game(size)
    board.add_mines(mines)
    board.board_setup()
    board.console_display_board()
    board.console_display_mask()
    return board


def setup_board():
    buttons = []
    count = 0
    for button in range(size * 5):
        button = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                        command=lambda: b_click(button))
        buttons.insert(0, button)
        count += 1

    row = 0
    col = 0
    for button in buttons:
        if col >= size:
            col = 0
            row += 1
        button.grid(row=row, column=col)
        col += 1


# Button clicked function
def b_click(b):
    pass


board = start_game(size, mines)
window = Tk()
window.title("Minesweeper")
# Add this in once i make an icon --> window.iconbitmap('file path')

# Build buttons
setup_board()

window.mainloop()

print("Guess where a bomb is")

print("Row:")
row = int(input())

print("Column:")
col = int(input())

board.reveal_position(row, col)

board.console_display_mask()

print("Guess where a bomb is")

print("Row:")
row = int(input())

print("Column:")
col = int(input())

board.set_flag_location(row, col)

board.console_display_mask()
