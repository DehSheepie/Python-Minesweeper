from tkinter import *
from game import Game


class GameWindow:
    def __init__(self):
        self.window = Tk()
        self.mines = 0
        self.size = 0
        self.window.title("Minesweeper")
        self.set_difficulty_easy()
        self.buttons = []
        self.game = Game(self.size)
        self.game.add_mines(self.mines)
        self.game.board_setup()
        self.game.console_display_board()
        self.game.console_display_mask()

    def setup_board(self):
        count = 0
        for button in range(self.size * self.size):
            # button = Button(window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace")
            # button.configure(command=lambda pass_button=button: b_click(w, pass_button))
            # button.bind('Button-1>', left)
            # button.bind('<Button-3>', right)
            button = Label(self.window, width=8, height=4, background="gray")
            self.buttons.insert(0, button)
            count += 1

        row = 0
        col = 0
        for button in self.buttons:
            if col >= self.size:
                col = 0
                row += 1
            button.grid(row=row, column=col)
            button['text'] = self.game.get_position(row, col)
            button.bind("<Button-1>", lambda event, row_num=row, col_num=col: self.left(event, row_num, col_num))
            button.bind("<Button-2>", lambda event, row_num=row, col_num=col: self.right(event, row_num, col_num))
            button.bind("<Button-3>", lambda event, row_num=row, col_num=col: self.right(event, row_num, col_num))
            col += 1

    def hint(self):
        self.game.get_hint()
        self.update_board()

    def update_board(self):
        row = 0
        col = 0
        for button in self.buttons:
            if col >= self.size:
                col = 0
                row += 1
            button.grid(row=row, column=col)
            button['text'] = self.game.get_position(row, col)
            if button['text'] is 'F':
                button.config(bg="orange")
            elif button['text'] is 0:
                button.config(bg="white")
            elif button['text'] is -1:
                button.config(bg="red")
            else:
                button.config(bg="gray")
            col += 1

    def create_menu(self):
        menu = Menu(self.window, tearoff=0)

        # Set up game menu
        game_menu = Menu(menu, tearoff=0)
        game_menu.add_command(label='Restart', command=self.restart_game)
        game_menu.add_command(label='Auto-hint')
        game_menu.add_command(label='Hint', command=self.hint)

        # Set up difficulty menu
        difficulty_menu = Menu(menu, tearoff=0)
        difficulty_menu.add_command(label="Easy", command=self.set_difficulty_easy)
        difficulty_menu.add_command(label="Medium", command=self.set_difficulty_medium)
        difficulty_menu.add_command(label="Hard", command=self.set_difficulty_hard)

        # Set up help menu
        help_menu = Menu(menu, tearoff=0)
        help_menu.add_command(label="")

        # Add game menu to the main menu
        menu.add_cascade(label='Game', menu=game_menu)

        # Add difficulty menu to the main menu
        menu.add_cascade(label="Difficulty", menu=difficulty_menu)

        menu.add_command(label='Exit', command=self.window.quit)

        self.window.config(menu=menu)

    def set_difficulty_hard(self):
        self.size = 10
        self.mines = 15
        for widget in self.window.winfo_children():
            widget.destroy()
        self.create_menu()
        self.buttons = []
        self.game = Game(self.size)
        self.game.add_mines(self.mines)
        self.game.board_setup()
        self.game.console_display_board()
        self.game.console_display_mask()
        self.setup_board()

    def set_difficulty_medium(self):
        self.size = 7
        self.mines = 9
        for widget in self.window.winfo_children():
            widget.destroy()
        self.create_menu()
        self.buttons = []
        self.game = Game(self.size)
        self.game.add_mines(self.mines)
        self.game.board_setup()
        self.game.console_display_board()
        self.game.console_display_mask()
        self.setup_board()

    def set_difficulty_easy(self):
        self.size = 4
        self.mines = 5
        for widget in self.window.winfo_children():
            widget.destroy()
        self.create_menu()
        self.buttons = []
        self.game = Game(self.size)
        self.game.add_mines(self.mines)
        self.game.board_setup()
        self.game.console_display_board()
        self.game.console_display_mask()
        self.setup_board()

    def restart_game(self):
        self.game.reset_game(self.size, self.mines)
        self.update_board()

    # Left click
    def left(self, event, row, col):
        print(row, col)
        print("clicked at", event.x, event.y)
        self.game.reveal_position(row, col)
        self.update_board()

    # Right click
    def right(self, event, row, col):
        print(row, col)
        print("clicked at", event.x, event.y)
        self.game.toggle_flag_location(row, col)
        self.update_board()


board = GameWindow()
board.setup_board()
board.create_menu()

# Add this in once i make an icon --> window.iconbitmap('file path')

board.window.mainloop()
