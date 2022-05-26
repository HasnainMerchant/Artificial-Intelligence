# Assignment 1 Part 2 - Generating Odd Magic Square
# Name - Hasnain Merchant       Div - B     Roll No - 30

import time
from os import system

def checkMagicSquare(magic_square, N):
    magic_sqaure_sum = N * ((N ** 2) + 1) / 2

    row_flag = 0
    # Check for Row Sum
    for i in range(N):
        row_sum = 0
        for j in range(N):
            row_sum += magic_square[i][j]
        if row_sum == magic_sqaure_sum:
            row_flag += 1

    column_flag = 0
    # Check for Column Sum
    for i in range(N):
        column_sum = 0
        for j in range(N):
            column_sum += magic_square[j][i]
        if column_sum == magic_sqaure_sum:
            column_flag += 1

    diag_flag = 0
    diag_sum = 0
    # Check for Diagonal Sum
    for i in range(N):
        diag_sum += magic_square[i][i]
    if diag_sum == magic_sqaure_sum:
        diag_flag += 1

    if row_flag == N and column_flag == N and diag_flag == 1:
        print("\n"*5)
        print(str(N) + " X " + str(N) + " Magic Square Is - ")
        for i in range(N):
            print(magic_square[i])
        print("\n")
    else:
        print("This Is Not A Magic Square")

def oddMagicSquare():
    N = int(input("Enter N for Magic Sqaure Matrix - "))

    magic_square = [[0 for x in range(N)]
                    for y in range(N)]

    # Calculate Initial Position For First Number
    num = 1
    row = 0
    column = N // 2

    while num <= N * N:

        print("\n\n\n")
        # Place The First Element
        magic_square[row][column] = num
        print()
        print("Step " + str(num) + " --")
        for i in range(N):
            print(magic_square[i])
        time.sleep(3)

        num += 1
        # Place The Next Element North-East Of The Current Element
        # New Column Value Is
        new_column = (column + 1) % N
        new_row = (row - 1) % N

        # If Element is Already There, Go South
        if magic_square[new_row][new_column]:
            row += 1
        else:
            row = new_row
            column = new_column
    checkMagicSquare(magic_square, N)

#Main Calling Function
oddMagicSquare()