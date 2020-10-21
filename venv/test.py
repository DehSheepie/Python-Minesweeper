from test2 import Test

d = Test("The test class")

print(type(d))
print(d.get_name())

array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(array[1][0])


def start_game():
    b = Game(size)
    b.add_mines(mines)
    b.board_setup()
    b.console_display_board()
    b.console_display_mask()
    return b


def restart_game(game_board):
    start_game()
    update_board(game_board)


def setup_board(b, w):
    count = 0
    for button in range(size * 5):
        # button = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
        # button.configure(command=lambda pass_button=button: b_click(w, pass_button))
        # button.bind('Button-1>', left)
        # button.bind('<Button-3>', right)
        button = Label(window, width=8, height=4, background="gray")
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
        if button['text'] is 'F':
            button.config(bg="orange")
        if button['text'] is 0:
            button.config(bg="white")
        if button['text'] is -1:
            button.config(bg="red")
        col += 1

# Left click
def left(event, row, col, game_board):
    print(row, col)
    print("clicked at", event.x, event.y)
    game_board.reveal_position(row, col)
    update_board(game_board)


# Right click
def right(event, row, col, game_board):
    print(row, col)
    print("clicked at", event.x, event.y)
    game_board.toggle_flag_location(row, col)
    update_board(game_board)