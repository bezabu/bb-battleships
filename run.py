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
    board_size = 8
    player_name = input('Enter your name:')
    player_score = 0
    computer_score = 0
    player_ships = []
    computer_ships = []
    board_label = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
    player_board = []
    for n in range(board_size):
        newlist = []
        player_board.append(newlist)
        for m in range(board_size):
            player_board[n].append("P") 
    computer_board = []
    for n in range(board_size):
        newlist = []
        computer_board.append(newlist)
        for m in range(board_size):
            computer_board[n].append("C") 

    def print_boards(self):
        print(f"      {self.player_name}'s board")
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


example_ansi = ANSI.background(
    ANSI, 97) + ANSI.color_text(ANSI, 96) + "HELLO " + GAME.player_name
print("\n")
GAME.print_boards(GAME)