from tkinter import *
from game import Game

size = 5
mines = 3
buttons = []
left_or_right = 0   # 0 is left, 1 is right


def start_game(game_size, mines_num):
    b = Game(game_size)
    b.add_mines(mines_num)
    b.board_setup()
    b.console_display_board()
    b.console_display_mask()
    return b


def setup_board(b, w):
    count = 0
    for button in range(size * 5):
        #button = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
        #button.configure(command=lambda pass_button=button: b_click(w, pass_button))
        #button.bind('Button-1>', left)
        #button.bind('<Button-3>', right)
        button = Label(window, width=10, height=10, background="gray")
        b.insert(0, button)
        count += 1

    row = 0
    col = 0
    for button in buttons:
        if col >= size:
            col = 0
            row += 1
        button.grid(row=row, column=col)
        button['text'] = w.get_position(row, col)
        button.bind("<Button-1>", lambda event, row_num=row, col_num=col: left(event, row_num, col_num, w))
        button.bind("<Button-2>", lambda event, row_num=row, col_num=col: right(event, row_num, col_num, w))
        button.bind("<Button-3>", lambda event, row_num=row, col_num=col: right(event, row_num, col_num, w))
        col += 1


def update_board(b):
    row = 0
    col = 0
    for button in buttons:
        if col >= size:
            col = 0
            row += 1
        button.grid(row=row, column=col)
        button['text'] = b.get_position(row, col)
        col += 1


def left(event, row, col, game_board):
    print(row, col)
    print("clicked at", event.x, event.y)
    game_board.reveal_position(row, col)
    update_board(game_board)


def right(event, row, col, game_board):
    print(row, col)
    print("clicked at", event.x, event.y)
    game_board.set_flag_location(row, col)
    update_board(game_board)

# Button clicked function
def b_click(game_board, button):
    b_row = button.grid_info()['row']
    b_col = button.grid_info()['column']
    if left_or_right is 0:
        game_board.reveal_position(b_row, b_col)
        update_board(game_board)
    else:
        game_board.set_flag_location(b_row, b_col)
        update_board(game_board)

board = start_game(size, mines)
window = Tk()
window.title("Minesweeper")
# Add this in once i make an icon --> window.iconbitmap('file path')

# Build buttons
setup_board(buttons, board)

window.mainloop()
