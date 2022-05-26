# Assignment 1 Part 4 - Tic-Tac-Toe AI Technique using MiniMax Algorithm
# Name - Hasnain Merchant       Div - B     Roll No - 30

player, opponent = 'X', 'O'

# Function To Print The Board
def printBoard(board):

    print(f"""\n    
              {board[1]}  |   {board[2]}   |  {board[3]}    
            -----|-------|------
              {board[4]}  |   {board[5]}   |  {board[6]}   
            -----|-------|------
              {board[7]}  |   {board[8]}   |  {board[9]}   \n""")


# This Function checks if moves can be made
def isMovesLeft(board):
    for i in range(1, 10):
            if board[i] == " ":
                return True
    return False


# This Function Returns Utility Value after Checking For Wins
def utility_function(b):
    # Checking for Rows for X or O victory.
    if (b[1] == b[2] == b[3] == player) or (b[4] == b[5] == b[6] == player) or (b[7] == b[8] == b[9] == player):
        return 10
    elif (b[1] == b[2] == b[3] == opponent) or (b[4] == b[5] == b[6] == opponent) or (b[7] == b[8] == b[9] == opponent):
        return -10

    # Checking for Columns for X or O victor
    if (b[1] == b[4] == b[7] == player) or (b[2] == b[5] == b[8] == player) or (b[3] == b[6] == b[9] == player):
        return 10
    elif (b[1] == b[4] == b[7] == opponent) or (b[2] == b[5] == b[8] == opponent) or (b[3] == b[6] == b[9] == opponent):
        return -10

    # Checking for Diagonals for X or O victory.
    if (b[1] == b[5] == b[9] == player) or (b[3] == b[5] == b[6] == player):
        return 10
    elif (b[1] == b[5] == b[9] == opponent) or (b[3] == b[5] == b[6] == opponent):
        return -10

    # Else if none of them have won then return 0
    return 0


# This Is The MiniMax Function
def MiniMax(board, depth, isMax):
    score = utility_function(board)

    # If Maximizer or 'X' has won the game return score 10
    if (score == 10):
        return score

    # If Minimizer or 'O' has won the game return score -10
    if (score == -10):
        return score

    # If there are no more moves and no winner then
    # it is a tie
    if (isMovesLeft(board) == False):
        return 0

    # If This Maximizer's Move
    if (isMax):
        best = -1000

        # Traverse all cells
        for i in range(1, 10):

            # Check if cell is empty
            if (board[i] == " "):
                # Make the move
                board[i] = player

                print("\t\tBoard Configuration When " + player + " Played At Position " + str(i))
                printBoard(board)

                # Call minimax recursively and choose
                # the maximum value
                best = max(best, MiniMax(board, depth + 1, not isMax))
                print("\t\tUtility Value Is : " + str(best) + "\n\n")

                # Undo the move
                board[i] = " "
        return best

    # If This Minimizer's Move
    else:
        best = 1000

        # Traverse all cells
        for i in range(1, 10):
            # Check if cell is empty
            if (board[i] == " "):
                # Make the move
                board[i] = opponent

                print("\t\tBoard Configuration When " + opponent + " Played At Position " + str(i))
                printBoard(board)

                # Call minimax recursively and choose
                # the minimum value
                best = min(best, MiniMax(board, depth + 1, not isMax))
                print("\t\tUtility Value Is : " + str(best) + "\n\n")
                # Undo the move
                board[i] = " "
        return best


# Function To Find Best Move For The Player
def findBestMove(board):
    bestval = -1000
    bestmove = -1
    branch = 1

    # Evaluate MiniMax Functions For All Possible Moves
    for i in range(1, 10):
        # Check If Cell Is Empty
        if board[i] == " ":

            # Make The Move
            board[i] = player

            print("\n\n\n\n\nFOR "+ str(branch) +" BRANCH\n\n")
            print("\t\tBoard Configuration When " + player + " Played At Position " + str(i))
            printBoard(board)

            # Compute Evaluation Function For This Move
            moveval = MiniMax(board, 0, False)


            # Undo The Move To Check For The Next Possible Moves
            board[i] = " "
            branch += 1

            # If The Value Of The Current Move Is More Than The Best Value, Then Update Best
            if moveval > bestval:
                bestmove = i
                bestval = moveval
    return bestmove


# Main code
board = {
        1: "X", 2: "O", 3: "X",
        4: "O", 5: " ", 6: "O",
        7: " ", 8: "X", 9: " "
}

bestMove = findBestMove(board)

print("The Optimal Move To Be Played Is At Position : " + str(bestMove) + "\n")