# Assignment 1 Part 3 - N-Queen Problem Using Backtracking Non-AI Technique
# Name - Hasnain Merchant       Div - B     Roll No - 30

import copy
import random

def get_board(n):
    # Returns an N by N board
    board = ["-"] * n
    for i in range(n):
        board[i] = ["-"] * n
    return board


def print_solution(solutions, n):
    # Prints one of the solutions randomly
    for x in range(len(solutions)):
        for row in solutions[x]:
            print(" ".join(row))
        print()
        print()

def printBoard(board):
    # Print The Board
    for i in board:
        print(" ".join(i))
    print()
    print()


def solve(board, column, n):
    # Use Backtracking To Find All Solutions
    printBoard(board)
    if column >= n:
        return

    for row in range(n):
        #Check If We Can Place At This Position or Not
        if is_safe(board, row, column, n):
            board[row][column] = "Q"
            print("Placed Queen At " + str(column+1) + " " + str(row+1))
            if column == n - 1:
                printBoard(board)
                add_solution(board)
                print("\t\t\t\t\tSOLUTION FOUND\n\n")
                board[row][column] = "-"
                return
            solve(board, column + 1, n)  # Recursive Call
            # Backtrack if we cant place the Queen
            board[row][column] = "-"
            print("Cannot Place Queen At This Position\n\n\t\t***BACKTRACKING QUEEN " + str(column+1) + " ***\n\n")


def is_safe(board, row, col, n):
    # Check If It's Safe To Place A Queen At board[row][column]

    # Check Row On Left Side
    for j in range(col):
        if board[row][j] == "Q":
            return False

    # Check Column
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i = i - 1
        j = j - 1

    # Check Diagonal
    x, y = row, col
    while x < n and y >= 0:
        if board[x][y] == "Q":
            return False
        x = x + 1
        y = y - 1

    return True


def add_solution(board):
    # Saves the board state to the global variable: solutions
    global solutions
    saved_board = copy.deepcopy(board)
    solutions.append(saved_board)


# Taking Size Of The Chessboard From User
n = int(input("Enter Size Of Board (Should Be Greater Than or Equal to 4) - "))

# Returns A Square Board of NxN dimension
board = get_board(n)

# List Of All Possible Solutions
solutions = []

# Solving The N-Queen Problem
print("ADDING QUEENS COLUMN WISE INSTEAD OF ROW WISE")
solve(board, 0, n)

print("\t\t\tCOMPLETED ALL COMBINATIONS\n\n")
print("The Final Solutions ARE : \n")
print_solution(solutions, n)