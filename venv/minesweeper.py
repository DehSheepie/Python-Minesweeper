from tkinter import *
from game import Game


class GameWindow:
    def __init__(self):
        self.auto_hint = True
        self.window = Tk()
        self.mines = 3
        self.size = 4
        self.window.title("Minesweeper")
        self.create_menu()
        self.buttons = []
        self.game = Game(self.size)
        self.game.add_mines(self.mines)
        self.game.board_setup()
        self.game.console_display_board()
        self.game.console_display_mask()

    # Sets up the minesweeper window
    def setup_board(self):
        # Creates a button for every space and adds it to the start of the buttons array
        for button in range(self.size * self.size):
            button = Label(self.window, width=8, height=4, background="gray")
            self.buttons.insert(0, button)
        row = 0
        col = 0
        # Loops through the buttons array and aligns and sets up each of the labels
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
        if self.auto_hint:
            self.hint()

    # Checks whether a hint could be found and returns a popup message if one couldn't be
    def hint(self):
        if self.game.get_hint():
            self.update_board()
            return True

        popup = Toplevel()
        popup.geometry("200x100")
        popup.title("Sorry")

        label = Label(popup, text="Could not find a hint.")
        label.pack(pady=10, padx=10)

        okay = Button(popup, text="Okay", command=popup.destroy)
        okay.pack(pady=20)

        popup.lift(self.window)

        return False

    def update_board(self):
        row = 0
        col = 0
        for button in self.buttons:
            # col increments each time the for loop is iterated through
            # If col exceeds the size of a row the col number is reset to 0 and the row number is incremented
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

    # Shows a popup message depending on whether the game is won or not
    def check_game_over(self):
        if self.game.game_over:
            if self.game.success is False:
                popup = Toplevel()
                popup.geometry("250x80")
                popup.title("Oh no!")

                label = Label(popup, text="You clicked on a mine. It is game over.")
                label.pack(pady=5, padx=10)

                restart = Button(popup, text="Restart", command=lambda: [popup.destroy(), self.restart_game()])
                restart.pack(pady=5)

                popup.lift(self.window)
            else:
                popup = Toplevel()
                popup.geometry("250x80")
                popup.title("Well done!")

                label = Label(popup, text="You found all the clear spaces. You win!")
                label.pack(pady=5, padx=10)

                restart = Button(popup, text="Restart", command=lambda: [popup.destroy(), self.restart_game()])
                restart.pack(pady=5)

                popup.lift(self.window)

    def create_menu(self):
        menu = Menu(self.window, tearoff=0)

        # Set up game menu
        game_menu = Menu(menu, tearoff=0)
        game_menu.add_command(label='Restart', command=self.restart_game)
        game_menu.add_command(label='Hint', command=self.hint)

        # Set up difficulty menu
        difficulty_menu = Menu(menu, tearoff=0)
        difficulty_menu.add_command(label="Easy", command=self.set_difficulty_easy)
        difficulty_menu.add_command(label="Medium", command=self.set_difficulty_medium)
        difficulty_menu.add_command(label="Hard", command=self.set_difficulty_hard)

        # Set up help menu
        help_menu = Menu(menu, tearoff=0)
        help_menu.add_command(label="")

        # Set up Auto hint menu
        auto_hint_menu = Menu(menu, tearoff=0)
        auto_hint_menu.add_command(label="On", command=self.auto_hint_on)
        auto_hint_menu.add_command(label="Off", command=self.auto_hint_off)

        # Add game menu to the main menu
        menu.add_cascade(label='Game', menu=game_menu)

        # Add difficulty menu to the main menu
        menu.add_cascade(label="Difficulty", menu=difficulty_menu)

        # Add hint menu to main menu
        game_menu.add_cascade(label="Auto Hint", menu=auto_hint_menu)

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
        self.mines = 3
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
        if self.auto_hint:
            if not self.hint():
                self.update_board()
        self.update_board()

    # Left click
    def left(self, event, row, col):
        print(row, col)
        print("clicked at", event.x, event.y)
        self.game.reveal_position(row, col)
        self.update_board()
        self.check_game_over()

    # Right click
    def right(self, event, row, col):
        print(row, col)
        print("clicked at", event.x, event.y)
        self.game.toggle_flag_location(row, col)
        self.update_board()

    def auto_hint_on(self):
        self.auto_hint = True

    def auto_hint_off(self):
        self.auto_hint = False


board = GameWindow()
board.setup_board()
board.create_menu()
# Add this in once i make an icon --> window.iconbitmap('file path')
board.window.mainloop()
