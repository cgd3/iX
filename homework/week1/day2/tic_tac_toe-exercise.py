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
    space = [1,2,3,4,5,6,7,8,9]
    wins = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8),(2,4,6))
    over = False 
    
    def board():
        print(space[0], space[1], space[2])
        print(space[3], space[4], space[5])
        print(space[6], space[7], space[8])
        print()
    
    def first_player():
        n = choose_space()
        if space[n] == "X" or space[n] == "O":
            print("\nSpace filled, try again." )
            first_player()
        else: 
            space[n] = "X"
    
    def second_player():
        n = choose_space()
        if space[n] == "X" or space[n] == "O":
            print("\nSpace filled, try again." )
            second_player()
        else: 
            space[n] = "O"
    
    def choose_space():
            while True: 
                value = input()
                try: 
                    value = int(value) - 1
                    if -1 < value < len(space):
                        return value
                    else:
                        print("\n Invalid space, try again.")
                        continue 
                except ValueError:
                    print("\n Invalid space, try again.")
                    continue
    
    def check_win():
        count = 0
        for a in wins:
            if space[a[0]] == space[a[1]] == space[a[2]] == "X":
                print ("Player 1 Wins\n")
                return True
            if space[a[0]] == space[a[1]] == space[a[2]] == "O":
                print("Player 2 Wins\n")
                return True
        for a in range(9):
            if space[a] == "X" or space[a] == "O": 
                count += 1
            if count == 9:
                print("Tie")
                return True
    while not over:
        board()
        over = check_win()
        if over == True:
            break
        print("Player 1 Turn")
        first_player()
        print()
        board()
        over = check_win()
        if over == True:
            break
        print("Player 2 Turn")
        second_player()
        print()
        
game()
    

