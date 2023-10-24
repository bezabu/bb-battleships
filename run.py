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
    board_size = 5
    player_name = input('Enter your name:')
    player_score = 0
    computer_score = 0
    player_ships = []
    computer_ships = []
    player_board = []
    computer_board = []


example_ansi = ANSI.background(
    ANSI, 97) + ANSI.color_text(ANSI, 96) + "HELLO " + GAME.player_name
print(example_ansi)
