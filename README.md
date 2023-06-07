
# Tic-Tac-Toe

This is a command-line implementation of the classic game Tic-Tac-Toe. The game allows a player to play against a computer AI.

## How to Play

1. The game board is represented by a 3x3 grid, numbered from 1 to 9 as follows:
```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

2. To make a move, enter the position number where you want to place your mark ('X'). The computer AI will automatically make its move.

3. The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins the game. If all positions on the board are filled and no player has won, the game ends in a draw.

4. After each game, the scoreboard will be displayed, showing the number of wins for the player, computer, and ties.

5. You can choose to play again or exit the game when prompted.

## Prerequisites

- Python 3.x



## Customization

You can modify the game behavior by changing the following variables in the `tictactoe.py` file:

- `player` and `computer`: The symbols used for the player and computer AI, respectively.
- `board`: The initial state of the game board.
- `player_score`, `computer_score`, and `tie_score`: The initial scores for the player, computer, and ties, respectively.

Feel free to explore and modify the code to enhance the game or add new features
