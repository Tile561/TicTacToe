board = {
    1: '.', 2: '.', 3: '.',
    4: '.', 5: '.', 6: '.',
    7: '.', 8: '.', 9: '.'
}

# Score variables
player_score = 0
computer_score = 0
tie_score = 0

def printBoard(board):
    # Prints the board
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("---+---+---")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("---+---+---")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("\n")

def isSpaceFree(position):
    # Checks if there is a free space on the board
    if board[position] == '.':
        return True
    else:
        return False

def checkForWin():
    # Checks for a win
    if (
        (board[1] == board[2] == board[3] != '.') or
        (board[4] == board[5] == board[6] != '.') or
        (board[7] == board[8] == board[9] != '.') or
        (board[1] == board[4] == board[7] != '.') or
        (board[2] == board[5] == board[8] != '.') or
        (board[3] == board[6] == board[9] != '.') or
        (board[1] == board[5] == board[9] != '.') or
        (board[7] == board[5] == board[3] != '.')
    ):
        return True
    else:
        return False

def checkWhichMarkWon(mark):
    if (
        (board[1] == board[2] == board[3] == mark) or
        (board[4] == board[5] == board[6] == mark) or
        (board[7] == board[8] == board[9] == mark) or
        (board[1] == board[4] == board[7] == mark) or
        (board[2] == board[5] == board[8] == mark) or
        (board[3] == board[6] == board[9] == mark) or
        (board[1] == board[5] == board[9] == mark) or
        (board[7] == board[5] == board[3] == mark)
    ):
        return True
    else:
        return False

def checkDraw():
    # Checks for a draw
    for key in board.keys():
        if board[key] == '.':
            return False
    return True

player = 'X'
computer = 'O'

def insertLetter(letter, position):
    # Inserts X or O
    if isSpaceFree(position):
        board[position] = letter
        printBoard(board)

        if checkDraw():
            print("Draw!")
            return 'tie'

        if checkForWin():
            if letter == 'X':
                print("Player wins!")
                return 'player'
            else:
                print("Computer wins!")
                return 'computer'

    return None

def playerMove():
    # Allows the player to move
    position = int(input("Enter the position for 'X'(0-9):  "))
    while position < 1 or position > 9 or not isSpaceFree(position):
        print("Invalid move. Try again.")
        position = int(input("Enter the position for 'X'(0-9):  "))

    result = insertLetter(player, position)
    return result

def computerMove():
    # The AI implementation of the computer player
    bestScore = -float('inf')
    bestMove = 0

    for key in board.keys():
        if board[key] == '.':
            board[key] = computer
            score = minimax(board, 0, False)
            board[key] = '.'
            if score > bestScore:
                bestScore = score
                bestMove = key

    insertLetter(computer, bestMove)

def minimax(board, depth, isMaximizing):
    # Minimax Algorithm
    if checkWhichMarkWon(computer):
        return 1
    elif checkWhichMarkWon(player):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -float('inf')
        for key in board.keys():
            if board[key] == '.':
                board[key] = computer
                score = minimax(board, depth + 1, False)
                board[key] = '.'
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = float('inf')
        for key in board.keys():
            if board[key] == '.':
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = '.'
                if score < bestScore:
                    bestScore = score
        return bestScore

print("Welcome to Tic-Tac-Toe!")
print("Positions are as follows:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
printBoard(board)
print("\n")

# Main game loop
while True:
    # Reset the board
    board = {
        1: '.', 2: '.', 3: '.',
        4: '.', 5: '.', 6: '.',
        7: '.', 8: '.', 9: '.'
    }

    print("Player goes first! Good luck.")

    while True:
        result = None
        result = playerMove()
        if result == 'player':
            player_score += 1
            break
        elif result == 'tie':
            tie_score += 1
            break
        computerMove()
        result = checkForWin()
        if result:
            computer_score += 1
            break

    print("Scoreboard:")
    print(f"Player: {player_score}  Computer: {computer_score}  Tie: {tie_score}")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        break
