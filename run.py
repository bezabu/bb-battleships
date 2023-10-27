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
    player_ships = []
    computer_ships = []
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
        print("Please set the size of the game board.\n")
        self.board_size = get_board_size()
        self.make_boards()
        # GAME.player_name = input('Enter your name:')
        # print(f"\nHello {GAME.player_name}!\n")

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
        print(f"    {self.player_name}'s board" + self.blank * (
            35 - len(self.player_name)) + "Computer's board")
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
                line_print_1 += " " + str(self.player_board[0][m]) + " │"
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
                line_print_1 += " " + str(self.computer_board[0][m]) + " │"
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


def get_board_size():
    while True:
        size = input("Please enter a number between 5 and 7: ")
        if validate_size(size):
            print(f"Board size set to {size} x {size}")
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
            print(f"\nHello {name}!\n")
            break
    return name


def main():
    game = GAME(7)
    game.print_boards()


# example_ansi = ANSI.background(
    # ANSI, 97) + ANSI.color_text(ANSI, 96) + "HELLO " + GAME.player_name
main()
