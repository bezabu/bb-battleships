import random
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


class ANSI():
    def background(self, code):
        return "\33[{code}m".format(code=code)

    def style_text(self, code):
        return "\33[{code}m".format(code=code)

    def color_text(self, code):
        return "\33[{code}m".format(code=code)


class GAME():
    # player_name = ""
    blank = " "
    # board_size = 7
    player_score = 0
    computer_score = 0
    # player_ships = []
    # computer_ships = []
    board_label = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
    blank = " "

    def __init__(self, board):
        print("Welcome to\n")
        f = open("banner.txt", "r")
        for x in f:
            print(ANSI.color_text(ANSI, 31) + x.replace('\n', ' '))
        f.close()
        print(ANSI.color_text(ANSI, 37) + "\n")
        self.player_name = get_name(self)
        print("Please set the size of the game board.")
        self.board_size = get_board_size()
        self.make_boards()
        # GAME.player_name = input('Enter your name:')
        # print(f"\nHello {GAME.player_name}!\n")
        print("Would you like to choose your ship locations?")
        while True:
            choose = input("Y/N: ").upper()
            if choose.__contains__('N'):
                print("Setting player ships...")
                self.player_ships = self.random_assign(self.board_size)
                break
            elif choose.__contains__('Y'):
                print("Enter ship location as letternumber,")
                print("for example: A1\n")
                self.player_ships = self.random_assign(self.board_size)
                break
            else:
                print("Please enter Y for yes or N for no.")
                False
        print("Setting computer ships...")
        self.computer_ships = self.random_assign(self.board_size)
        print(self.player_ships)
        self.set_board(self.player_board, self.player_ships)

    def set_board(self, board, ships):
        for n in ships:
            letter = ord(n[0]) - 64
            number = int(n[1])
            board[number-1][letter-1] = "@"

    def choose_ship(self):
        """
        Allow player to choose ship locations by entering char-int
        """

    def validate_name(self, vname):
        try:
            name = str(vname)
            if len(name) > 30:
                raise ValueError(
                    f"Name is {len(name)} characters,\nmust be less than 30"
                )
        except ValueError as e:
            print(f"Invalid data: {e}. Please try again.\n")
            return False
        return True

    def make_boards(self):
        self.player_board = []
        self.computer_board = []
        for n in range(self.board_size):
            self.newlist = []
            self.newlist2 = []
            self.player_board.append(self.newlist)
            self.computer_board.append(self.newlist2)
            for m in range(self.board_size):
                self.player_board[n].append("P")
                self.computer_board[n].append("C")

    def print_boards(self):
        blankspace = (((self.board_size*4)+9)*2)-24
        print(f" {self.player_name}'s board" + self.blank * (
            blankspace - len(self.player_name)) + "Computer's board")
        # upper label row
        # player
        line_print_0 = " ┌" + f"───┬"
        line_print_1 = " │" + f"   │"
        for n in range(self.board_size):
            line_print_0 += f"───┬"
            line_print_1 += f" {str(self.board_label[n])} │"
        line_print_0 += "───┐"
        line_print_1 += "   │"
        # computer
        line_print_0 += " ┌" + f"───┬"
        line_print_1 += " │" + f"   │"
        for n in range(self.board_size):
            line_print_0 += f"───┬"
            line_print_1 += f" {str(self.board_label[n])} │"
        line_print_0 += "───┐"
        line_print_1 += "   │"
        print(ANSI.color_text(ANSI, 32) + line_print_0)
        print(line_print_1)
        # main body of board
        # player
        for n in range(self.board_size):
            line_print_0 = " ├" + f"───┼"
            line_print_1 = " │" + f" {str(n+1)} │"
            line_print_3 = " ├" + f"───┼"
            for m in range(self.board_size):
                line_print_0 += "───┼"
                line_print_1 += " " + str(self.player_board[n][m]) + " │"
                line_print_3 += "───┴"
            line_print_0 += f"───┤"
            line_print_1 += f" {str(n+1)} │"
            line_print_3 += f"───┘"
            # computer
            line_print_0 += " ├" + f"───┼"
            line_print_1 += " │" + f" {str(n+1)} │"
            line_print_3 += " ├" + f"───┼"
            for m in range(self.board_size):
                line_print_0 += "───┼"
                line_print_1 += " " + str(self.computer_board[n][m]) + " │"
                line_print_3 += "───┴"
            line_print_0 += f"───┤"
            line_print_1 += f" {str(n+1)} │"
            line_print_3 += f"───┘"
            # print(line_print_0)
            # print(line_print_1)
            print(line_print_0)
            print(line_print_1)
        # lower label row
        # player
        line_print_0 = " ├" + f"───┼"
        line_print_1 = " │" + f"   │"
        for n in range(self.board_size):
            line_print_0 += f"───┼"
            line_print_1 += f" {str(self.board_label[n])} │"
        line_print_0 += "───┤"
        line_print_1 += "   │"
        # computer
        line_print_0 += " ├" + f"───┼"
        line_print_1 += " │" + f"   │"
        for n in range(self.board_size):
            line_print_0 += f"───┼"
            line_print_1 += f" {str(self.board_label[n])} │"
        line_print_0 += "───┤"
        line_print_1 += "   │"
        print(line_print_0)
        print(line_print_1)
        line_print_3 = " └" + "───┴"
        for m in range(self.board_size):
            line_print_3 += "───┴"
        line_print_3 += "───┘"
        line_print_3 += " └" + "───┴"
        for m in range(self.board_size):
            line_print_3 += "───┴"
        line_print_3 += "───┘"
        print(line_print_3)

    def random_assign(self, ship_count):
        ship_list = []
        letter_list = []
        for n in range(self.board_size):
            letter_list.append(self.board_label[n])
        for n in range(ship_count):
            while True:
                new_coord = make_coord(letter_list, self.board_size)
                if new_coord not in ship_list:
                    ship_list.append(new_coord)
                    break
        # print(ship_list)
        return ship_list


def make_coord(letters, maxnumber):
    cha = random.choice(letters)
    num = str(round(random.randrange(0, maxnumber))+1)
    return cha + num


def get_board_size():
    while True:
        size = input("Please enter a number between 5 and 7: ")
        if validate_size(size):
            print(f"Board size set to {size} x {size}\n")
            break
    return int(size)


def validate_size(vsize):
    try:
        size = int(vsize)
        if size < 5 or size > 7:
            raise ValueError(
                f"Board size must be between 5 and 7, you entered {size}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again.\n")
        return False
    return True


def get_name(owner):
    while True:
        name = input('Please enter your name:')
        if owner.validate_name(name):
            print(f"\nHello {name}!")
            break
    return name


def main():
    game = GAME(7)
    game.print_boards()
    game.random_assign(game.board_size)


# example_ansi = ANSI.background(
    # ANSI, 97) + ANSI.color_text(ANSI, 96) + "HELLO " + GAME.player_name
main()
