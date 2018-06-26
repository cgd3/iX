# -*- coding: utf-8 -*-
"""

Ejercicio. Tic-tac-toe

We are going to build a program that allows us to play tic-tac-toe on the terminal


In a nutshell, the tic-tac-toe board can be thought of 3 lists inside another one

board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
]

por ejemplo, si queremos ver cual es el estado de la casilla de arriba a la 
izquerda, podemos acceder haciendo tablero[[0,0]]

We have 2 players, and each player will alternate in choosing a different slot on the board,
and placing either an "X"  (player 1) or "O" (player 2)

The game will have to validate that the new coordinates chosen by the current player 
are valid, i.e., they need to be empty and be inside the board.


Hint: You can use a deque (in the module collections) to rotate between player 1 and 2
"""


def game():
    pass


if __name__ == "__main__":
    game()
