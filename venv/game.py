from random import randrange


# TODO: Fix error with the hint system so that redundant hints aren't given

# Set up array
def create_board(size):
    b = [[0] * size for n in range(size)]
    return b


def create_mask(size):
    m = [[False] * size for n in range(size)]
    return m


class Game:
    #   List of the 8 potential adjacent spaces
    positions = [[-1, -1], [-1, 0], [-1, +1], [0, -1], [0, +1], [+1, -1], [+1, 0], [+1, +1]]

    def __init__(self, size):
        self.spaces = (size * size)
        self.number_of_mines = 0
        self.board = create_board(size)  # The actual game board used by the program
        self.mask = create_mask(size)  # What the player sees
        self.flags = create_mask(size)  # Array where the player can add mine flags
        self.game_over = False
        self.success = False
        self.size = size

    def reset_game(self, size, mines):
        self.board = create_board(size)
        self.mask = create_mask(size)
        self.flags = create_mask(size)
        self.add_mines(mines)
        self.board_setup()
        self.game_over = False

    # Adds mines to the board. Takes the array and the number of mines to add
    def add_mines(self, n):
        size = len(self.board)
        mine_num = n
        # Continues the loop for the number of mines to be added
        while n > 0:
            find_new_mine_location = 3  # Number of attempts the program will make at finding a free location
            while find_new_mine_location > 0:
                x = randrange(size)
                y = randrange(size)
                if self.board[x][y] != -1:
                    self.board[x][y] = -1  # Currently using -1 to signify mines
                    find_new_mine_location = 0
                else:
                    print(f"Mine already in position {x}, {y}")
                    find_new_mine_location -= 1
            n -= 1
        self.number_of_mines = mine_num

    def check_success(self):
        count = 0
        for row in self.mask:
            for col in row:
                if col is True:
                    count += 1
        if not self.game_over and count >= self.spaces - self.number_of_mines:
            self.game_over = True
            self.success = True
            self.reveal_all()

    # Sets up the board and assigns the appropriate numbers to each space
    def board_setup(self):
        i_row = 0
        i_col = 0
        for row in self.board:
            i_col = 0
            for col in row:
                if col != -1:
                    self.board[i_row][i_col] = self.calculate_mine_proximity(i_row, i_col)
                i_col += 1
            i_row += 1

    # Calculates the number of mines in proximity with the given space
    def calculate_mine_proximity(self, row, col):
        value = 0
        size = len(self.board)
        for position in self.positions:
            if self.check_in_board_bounds(row + position[0], col + position[1]):
                if self.board[row + position[0]][col + position[1]] == -1:
                    value += 1
        return value

    # Checks that a given space is within the bounds of the game board
    def check_in_board_bounds(self, x, y):
        size = len(self.board)
        if x < 0 or y < 0:
            return False
        if x >= size or y >= size:
            return False
        return True

    # Displays the game board in the console
    def console_display_board(self):
        for row in self.board:
            print(row)

    # Displays the mask in the console
    def console_display_mask(self):
        i_row = 0
        i_col = 0
        for row in self.mask:
            i_col = 0
            output = self.board[i_row].copy()
            for col in row:
                if not col:
                    output[i_col] = '#'
                elif self.flags[i_row][i_col]:
                    output[i_col] = 'F'
                i_col += 1
            output = str(output).replace('\'', '')
            print(output)
            i_row += 1

    def get_position(self, row, col):
        if self.flags[row][col]:
            return 'F'
        elif self.mask[row][col]:
            return self.board[row][col]
        else:
            return '#'

    def reveal_position(self, row, col):
        if self.board[row][col] == 0 and not self.mask[row][col]:
            self.mask[row][col] = True
            for position in self.positions:
                if self.check_in_board_bounds(row + position[0], col + position[1]):
                    if self.board[row + position[0]][col + position[1]] == 0:
                        self.reveal_position(row + position[0], col + position[1])
                    else:
                        self.mask[row + position[0]][col + position[1]] = True
        elif self.board[row][col] == -1:
            self.mask[row][col] = True
            self.game_over = True
            self.check_success()
            self.reveal_all()
        else:
            self.mask[row][col] = True
            self.check_success()

    def reveal_all(self):
        self.mask = [[True] * self.size for n in range(self.size)]

    def get_hint(self):

        hint_locations = []
        i_row = 0
        i_col = 0
        for row in self.board:
            i_col = 0
            for col in row:
                if col == 0:
                    hint_locations.append([i_row, i_col])
                i_col += 1
            i_row += 1

        if hint_locations:
            i = randrange(len(hint_locations))
            print(hint_locations)
            self.reveal_position(hint_locations[i][0], hint_locations[i][1])
            return True
        else:
            return False

    def toggle_flag_location(self, row, col):
        if self.flags[row][col]:
            self.flags[row][col] = False
        else:
            self.flags[row][col] = True
