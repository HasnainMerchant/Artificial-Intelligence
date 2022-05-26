# Assignment 1 Part 1 - Non-AI Technique Tic-Tac-Toe
# Name - Hasnain Merchant       Div - B     Roll No - 30

from random import randint
from itertools import combinations

def new_board():
    global magic_square
    magic_square = {
        8: " ", 3: " ", 4: " ",
        1: " ", 5: " ", 9: " ",
        6: " ", 7: " ", 2: " "
    }

    global board
    board = {
        1: " ", 2: " ", 3: " ",
        4: " ", 5: " ", 6: " ",
        7: " ", 8: " ", 9: " "
    }

    global positions_played
    positions_played = {
        "X": [],
        "O": []
    }


def print_board(choice):

    if choice == 1:
        print(f"""\n    
          1  |   2   |  3    
        -----|-------|------
          4  |   5   |  6   
        -----|-------|------
          7  |   8   |  9   \n""")

    elif choice == 2:
        print(f"""\n    
          {board[1]}  |   {board[2]}   |  {board[3]}    
        -----|-------|------
          {board[4]}  |   {board[5]}   |  {board[6]}   
        -----|-------|------
          {board[7]}  |   {board[8]}   |  {board[9]}   \n""")


class Computer:

    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, move):
        move2 = magicSquarePosition(move)
        if board[move] == " ":
            board[move] = self.symbol
            magic_square[move2] = self.symbol
            positions_played[self.symbol].append(move2)
            return True
        else:
            return False

    def play_turn(self):
        move = self.check_for_win()
        if(move):
            self.make_move(move)
            return True
        else:
            self.make_random_move()
            print(f"\t\t\t{self.symbol} Made RANDOM move")
            return False

    def make_random_move(self):
        move = randint(1, 9)
        if (self.make_move(move)):
            return
        else:
            self.make_random_move()
        return

    def check_for_win(self):
        for i in range(0, len(positions_played[self.symbol]) - 1):
            for j in range(i + 1, len(positions_played[self.symbol])):
                win_pos = 15 - (positions_played[self.symbol][i] + positions_played[self.symbol][j])
                if (10 > win_pos > 0 and magic_square[win_pos] == " "):
                    return win_pos

def magicSquarePosition(move):
    magicSqaure = [0, 8, 3, 4, 1, 5, 9, 6, 7, 2]
    return magicSqaure[move]

class Player:

    def __init__(self, symbol):
        self.symbol = symbol

    def play_turn(self):
        move = int(input("Choose An Empty Position To Make A Move : "))
        move2 = magicSquarePosition(move)
        if board[move] == " ":
            board[move] = self.symbol
            magic_square[move2] = self.symbol
            positions_played[self.symbol].append(move2)
            if len(positions_played[self.symbol]) >= 3:
                for combination in combinations(positions_played[self.symbol], 3):
                    if sum(list(combination)) == 15:
                        return True
                return False
        else:
            print("Please Enter A Empty Position Number\n")
            self.play_turn()


def play_TTT():
    new_board()
    moves = 0
    win = False

    player = Player("X")
    comp = Computer("O")

    print_board(1)
    print_board(2)
    for i in range(1, 10):
        win = player.play_turn()
        moves += 1
        print_board(2)
        if win:
            print(f"Player ({player.symbol}) WINS !!!")
            break
        if moves == 9:
            break

        win = comp.play_turn()
        moves += 1
        print_board(2)
        if win:
            print(f"Player ({comp.symbol}) WINS !!!")
            break

    if win == False:
        print("Its a DRAW")

    if (input("\nPlay Again [Yes/No] : ") in ("Y")):
        play_TTT()


#Main Calling Function
play_TTT()