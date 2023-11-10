import random


class ANSI():
    """
    Refactored escape codes. Enables supplying just the colour
    code and the functions will return the entire escape codes.
    """
    def col_bck(self, code):
        """
        Returns ANSI escape code for background colouring.
        """
        return "\33[{code}m".format(code=code)

    def col_txt(self, code):
        """
        Returns ANSI escape code for text colouring.
        """
        return "\33[{code}m".format(code=code)


class GAME():
    """
    Class holding relevant game information and functions.
    """
    blank = " "
    player_score = 0
    computer_score = 0
    player_guesses = []
    computer_guesses = []
    board_label = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
    win = False
    winner = ""
    player_name = ""

    def __init__(self):
        """
        Create game instance and get player info and settings.
        """
        self.player_score = 0
        self.computer_score = 0
        self.player_guesses = []
        self.computer_guesses = []
        self.win = False
        print(ANSI.col_bck(ANSI, 0), end="")
        print("\n                                 Welcome to")
        f = open("banner.txt", "r")
        for x in f:
            print(ANSI.col_txt(ANSI, 31) + x.replace('\n', ' '))
        f.close()
        draw_art()
        print(ANSI.col_txt(ANSI, 37))
        self.player_name = get_name(self)
        print("Please set the size of the game board.")
        self.board_size = get_board_size()
        self.make_boards()
        print("Would you like to choose your ship locations?")
        while True:
            choose = input("Y/N: \n").upper()
            if 'N' in choose and 'Y' not in choose:
                print("Setting player ships...")
                self.player_ships = self.random_assign(self.board_size)
                break
            elif 'Y' in choose and 'N' not in choose:
                allowed = self.board_size
                used = 0
                self.player_ships = []
                print("Enter ship location as letternumber,")
                print("for example: A1")
                for _ in range(allowed):
                    print(self.print_boards(), end="")
                    print(f"{allowed - used} ships remaining.\n")
                    self.player_ships.append(self.choose_ship())
                    used += 1
                    self.set_board(self.player_board, self.player_ships)
                break
            else:
                print("Please enter Y for yes or N for no.")
                False
        print("Setting computer ships...")
        self.computer_ships = self.random_assign(self.board_size)
        self.set_board(self.player_board, self.player_ships)

    def set_board(self, board, ships):
        """
        Update the board with the ship positions.
        """
        for n in ships:
            letter = ord(n[0]) - 64
            number = int(n[1])
            board[number-1][letter-1] = "@"

    def choose_ship(self):
        """
        Allow player to choose ship locations by entering char-int.
        """
        while True:
            new_ship = input("Enter coordinates:\n").upper()
            if validate_coord(
                            new_ship,
                            self.board_size,
                            self.player_ships,
                            self):
                break
        return new_ship

    def validate_name(self, vname):
        """
        Check if name entered is less than 30 characters long.
        """
        try:
            name = str(vname)
            if len(name) > 30:
                raise ValueError(
                    f"Name is {len(name)} characters,\nmust be 30 or less"
                )
        except ValueError as e:
            print(f"Invalid data: {e}. Please try again.\n")
            return False
        return True

    def make_boards(self):
        """
        Create the 2 dimensional arrays to store board info.
        """
        self.player_board = []
        self.computer_board = []
        for n in range(self.board_size):
            self.newlist = []
            self.newlist2 = []
            self.player_board.append(self.newlist)
            self.computer_board.append(self.newlist2)
            for _ in range(self.board_size):
                self.player_board[n].append(" ")
                self.computer_board[n].append(" ")

    def print_boards(self):
        """
        Display the game boards by iterating over several lines.
        Returns the string to print.
        """
        buffer = ""
        buffer += ANSI.col_bck(ANSI, 47)
        buffer += ANSI.col_txt(ANSI, 30)
        blankspace = (((self.board_size*4)+9)*2)-24
        buffer += f" {self.player_name}'s board" + self.blank * (
            blankspace - len(self.player_name)) + "Computer's board "
        buffer += ANSI.col_txt(ANSI, 37)
        buffer += ANSI.col_bck(ANSI, 0) + "\n"
        # print(buffer, end="")
        # top row
        for n in range(2):
            line_print = " ┌"
            for m in range(self.board_size+1):
                line_print += "───┬"
            line_print += "───┐"
            buffer += ANSI.col_txt(ANSI, 32) + line_print
        buffer += "\n"
        buffer += label_line(self)
        buffer += label_line(self)
        buffer += "\n"
        buffer += new_line(self.board_size)
        buffer += new_line(self.board_size)
        buffer += "\n"
        # game row
        for n in range(self.board_size):
            # player
            buffer += " │"
            buffer += ANSI.col_txt(ANSI, 37)
            buffer += f" {str(n+1)} "
            buffer += ANSI.col_txt(ANSI, 32) + "│"
            for m in range(self.board_size):
                if str(self.player_board[n][m]) == "@":
                    if len(self.player_ships) < self.board_size:
                        buffer += ANSI.col_txt(ANSI, 33)
                    else:
                        # if computer has guessed here
                        b = str(self.board_label[m])+str(n+1)
                        if b in self.computer_guesses:
                            buffer += ANSI.col_txt(ANSI, 31)
                        else:
                            buffer += ANSI.col_txt(ANSI, 37)
                elif str(self.player_board[n][m]) == "X":
                    buffer += ANSI.col_txt(ANSI, 34)
                buffer += f" {str(self.player_board[n][m])}"
                buffer += ANSI.col_txt(ANSI, 32) + " │"
            buffer += ANSI.col_txt(ANSI, 37)
            buffer += f" {str(n+1)} "
            buffer += ANSI.col_txt(ANSI, 32) + "│"
            # computer
            buffer += " │"
            buffer += ANSI.col_txt(ANSI, 37) + f" {str(n+1)} "
            buffer += ANSI.col_txt(ANSI, 32) + "│"
            for m in range(self.board_size):
                if str(self.computer_board[n][m]) == "@":
                    buffer += ANSI.col_txt(ANSI, 31)
                elif str(self.computer_board[n][m]) == "X":
                    buffer += ANSI.col_txt(ANSI, 34)
                buffer += f" {str(self.computer_board[n][m])}"
                buffer += ANSI.col_txt(ANSI, 32) + " │"
            buffer += ANSI.col_txt(ANSI, 37) + f" {str(n+1)} "
            buffer += ANSI.col_txt(ANSI, 32) + "│"
            buffer += "\n"
            buffer += new_line(self.board_size)
            buffer += new_line(self.board_size)
            buffer += "\n"
        # bottom row
        buffer += label_line(self)
        buffer += label_line(self)
        buffer += "\n"
        line_print = ""
        for n in range(2):
            line_print += " └"
            for n in range(self.board_size+1):
                line_print += "───┴"
            line_print += "───┘"
        buffer += line_print + "\n"
        buffer += ANSI.col_txt(ANSI, 37)
        if self.board_size == 5:
            buffer += blank_lines(4)
        elif self.board_size == 6:
            buffer += blank_lines(2)
        return buffer

    def random_assign(self, ship_count):
        """
        Returns a list of randomly selected positions.
        """
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
        return ship_list


def draw_art():
    """
    Draw ASCII art of ship from txt file.
    """
    g = open("art.txt", "r")
    for x in g:
        print(ANSI.col_txt(ANSI, 37) + x.replace('\n', ' '))
    g.close()


def make_coord(letters, maxnumber):
    """
    Chooses a random coordinate.
    """
    cha = random.choice(letters)
    num = str(round(random.randrange(1, maxnumber+1)))
    return cha + num


def get_board_size():
    """
    Prompt the user to select a board size.
    """
    while True:
        size = input("Please enter a number between 5 and 7:\n")
        if validate_size(size):
            print(f"Board size set to {size} x {size}\n")
            break
    return int(size)


def validate_coord(coords, size, ships, gameself):
    """
    Validate user inputted coordinates to match game formatting.
    """
    try:
        if len(coords) == 2:
            for _ in coords:
                letter = ord(coords[0]) - 64
                number = int(coords[1])
                if letter < 1 or letter > size:
                    raise ValueError(f"{coords} is not a valid coordinate")
                if number < 1 or number > size:
                    raise ValueError(f"{coords} is not a valid coordinate")
                if coords in ships:
                    raise ValueError(f"{coords} already used")
        if len(coords) != 2:
            raise ValueError(f"{coords} is not 1 letter and 1 number")
    except ValueError as e:
        buffer = ""
        buffer += gameself.print_boards()
        buffer += f"Invalid data: {e}, please try again.\n"
        print(buffer)
        return False
    return True


def validate_size(vsize):
    """
    Ensure the board size in an integer between 5 and 7.
    """
    try:
        size = int(vsize)
        if size < 5 or size > 7:
            raise ValueError(
                f"Size must be either 5, 6 or 7. You entered {size}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}. \nPlease try again.\n")
        return False
    return True


def get_name(owner):
    """
    Prompt the user to enter their name, validate and return the name.
    """
    while True:
        name = input('Please enter your name:\n')
        if owner.validate_name(name):
            print(f"\nHello {name}!")
            print(blank_lines(2))
            break
    return name


def new_line(size):
    """
    For use in the print_boards function, returns an interior horizontal line.
    """
    buffer = ""
    buffer += " ├"
    for _ in range(size+1):
        buffer += "───┼"
    buffer += "───┤"
    return buffer


def label_line(owner):
    """
    For use in the print_boards function, returns a row
    of column labels.
    """
    buffer = ""
    buffer += " │   │"
    for n in range(owner.board_size):
        buffer += ANSI.col_txt(
            ANSI, 37) + f" {str(owner.board_label[n])} "
        buffer += ANSI.col_txt(ANSI, 32) + "│"
    buffer += "   │"
    return buffer


def blank_lines(num):
    """
    Prints empty strings to force a new line
    """
    lines = ""
    for _ in range(num):
        lines += "\n"
    return lines


def guess(owner, player):
    """
    Get input from the player, validate and compare to computer's ships.
    Updates the relevant lists and returns the message to display under
    the game boards.
    """
    guess = ""
    if player is True:
        ships = owner.player_guesses
        while True:
            guess = input("Enter coordinates:\n").upper()
            if validate_coord(guess, owner.board_size, ships, owner):
                break
    else:
        ships = owner.computer_guesses
        letter_list = []
        for n in range(owner.board_size):
            letter_list.append(owner.board_label[n])
        while True:
            guess = make_coord(letter_list, owner.board_size)
            if guess not in owner.computer_guesses:
                break
    letter = ord(guess[0]) - 64
    number = int(guess[1])
    if player is True:
        owner.player_guesses.append(guess)
        if guess in owner.computer_ships:
            # hit
            message = f"{ANSI.col_txt(ANSI, 37)}You chose {guess}..."
            message += f"{ANSI.col_txt(ANSI, 31)} Hit!"
            message += f"{ANSI.col_txt(ANSI, 37)}"
            owner.computer_board[number - 1][letter - 1] = "@"
            owner.player_score += 1
            if owner.player_score >= owner.board_size:
                owner.winner = f"{owner.player_name} won!"
                owner.win = True
        else:
            # miss
            message = f"{ANSI.col_txt(ANSI, 37)}You chose {guess}..."
            message += f"{ANSI.col_txt(ANSI, 34)} Miss!"
            message += f"{ANSI.col_txt(ANSI, 37)}"
            owner.computer_board[number - 1][letter - 1] = "X"
    if player is False:
        owner.computer_guesses.append(guess)
        if guess in owner.player_ships:
            # hit
            message = f"{ANSI.col_txt(ANSI, 37)}Computer chooses {guess}..."
            message += f"{ANSI.col_txt(ANSI, 31)} Hit!"
            message += F"{ANSI.col_txt(ANSI, 37)}"
            owner.computer_score += 1
            if owner.computer_score >= owner.board_size and owner.win is False:
                owner.winner = f"Computer won!"
                owner.win = True
        else:
            # miss
            message = f"{ANSI.col_txt(ANSI, 37)}Computer chooses {guess}..."
            message += F"{ANSI.col_txt(ANSI, 34)} Miss!"
            message += F"{ANSI.col_txt(ANSI, 37)}"
            owner.player_board[number - 1][letter - 1] = "X"
    return message


def game_loop(game):
    """
    Alternates between user and computer guesses until there is a winner,
    then calls the play_again function.
    """
    print(" ")
    while game.win is False:
        player_summary = guess(game, True)
        computer_summary = guess(game, False)
        buffer = ""
        buffer += game.print_boards()
        buffer += player_summary
        blankspace = ((4 * game.board_size) + 12) - 20
        buffer += game.blank * blankspace
        buffer += computer_summary + "\n"
        buffer += "Your turn! Enter a location as letternumber, "
        buffer += "for example: A1\n"
        print(buffer, end="")
    print(game.print_boards(), end="")
    print(game.winner)
    print("")
    play_again()


def play_again():
    """
    Asks the user if they want to play again.
    If yes, creates a new game instance.
    If no, exit the program.
    """
    while True:
        again = input("Would you like to play again? Y/N:\n").upper()
        if 'Y' in again and 'N' not in again:
            main()
            break
        elif 'N' in again and 'Y' not in again:
            print(blank_lines(2))
            draw_art()
            print(blank_lines(5))
            print("Thanks for playing!")
            quit()
        else:
            print("Please enter Y for yes or N for no.")
            False


def main():
    """
    Create a new game instance and start the game_loop function.
    """
    print("")
    game = GAME()
    print(game.print_boards(), end="")
    print("Your turn! Enter a location as letternumber,", end="")
    print("for example: A1")
    game_loop(game)


main()
