import numpy as np
import time
import random
import sys

win = False             ##value determines if the game is over (even by stalemate)
introchoice = False     ##value determines if we want the rules explained
replay = True           ##value determines if we should play again
correctagain = False    ##dummy value to make an error-catching 'continue' in the play again function operate properly. never changes.
firstchoice = False     ##values determines if the user has selected who should go first
array = [0,1,2]

compareboard = np.array([   ## what a new board looks like. used for checking if a stalemate has occurred.
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    ])

win1 = [1, 1, 1]
win2 = [2, 2, 2]
yes = ['Y', 'y', 'yes', 'YES', 'Yes']
no = ['N', 'n', 'no', 'NO', 'No']

while introchoice == False:
    choice = input("Welcome, challenger. Would you like me to explain the way our Tic-Tac-Toe game will work? (Y/N)")
            ##choosing 'no' or an equivalent will start the game. choosing 'yes' or an equivalent will run the below lines of explanation
    choice = choice.strip()
    if choice not in yes and choice not in no:
        print("Invalid selection. Please choose 'Yes' or 'No'.")
        continue
    if choice in no:
        introchoice = True
    if choice in yes:
        print("Alright. You will be the number '1' and I will be the number '2'...")
        time.sleep(3)
        print("You will choose your move by selecting the row and column, respectively, as 'rowcolumn'...")
        time.sleep(3)
        print("For example, if you want row '1' and column '2', enter '12'.")
        time.sleep(2)
        print("Remember, the rows and columns are numbered from 0 to 2, not 1 to 3!")
        time.sleep(3)
        print("Ready? Here we go!")
        time.sleep(1)
        introchoice = True

while firstchoice == False:
    first = input("Would you like to go first? (Y/N)")
    first = first.strip()
    if first not in yes and first not in no:
        print("Invalid selection. Please choose 'Yes' or 'No'.")
        continue
    if first in yes:
        while replay == True:
            board = np.array([  
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            ])
            while win == False:
                ##human's turn
                nextmove = str(input("Your turn: "))
                try:
                    int(nextmove[0])
                except:
                    print("Whoops! Please enter a valid move!")
                    continue
                try:
                    int(nextmove[1])
                except:
                    print("Whoops! Please enter a valid move!")
                    continue
                if int(nextmove[0]) not in array or int(nextmove[1]) not in array:
                    print("Please select a valid row and column! Try again...")
                    time.sleep(1)
                    continue
                elif board[int(nextmove[0])][int(nextmove[1])] != 0:
                    print("That spot is already taken! Please select again!")
                    time.sleep(1)
                    continue
                board[int(nextmove[0])][int(nextmove[1])] = 1
                print(board)
                time.sleep(1)
                if (board[0] == win1).all() == True or (board[1] == win1).all() == True or (board[2] == win1).all() == True: ##row win
                    print("You have won! Congratulations!")
                    win == True
                    break
                if (board[:,0] == win1).all() == True or (board[:,1] == win1).all() == True or (board[:,2] == win1).all() == True: ##col win
                    print("You have won! Congratulations!")
                    win == True
                    break
                if board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1: ##diag win
                    print("You have won! Congratulations!")
                    win == True
                    break
                if board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1: ##diag win
                    print("You have won! Congratulations!")
                    win == True
                    break
                if (board == compareboard).any() == False:
                    print("We have reached a stalemate! There is no winner!")
                    win == True
                    break
                ##computer's turn
                print("Here is my move...")
                time.sleep(1)
                goodcompmove = False
                while goodcompmove == False:
                    comprow = random.choice(array)
                    compcol = random.choice(array)
                    if board[comprow][compcol] != 0:
                        continue
                    else:
                        board[int(comprow)][int(compcol)] = 2
                        print(board)
                        time.sleep(1)
                        goodcompmove = True
                ##checking for a computer win or a stalemate
                if (board[0] == win2).all() == True or (board[1] == win2).all() == True or (board[2] == win2).all() == True:
                    print("You have lost. Better luck next time!")
                    win == True
                    break
                if (board[:,0] == win2).all() == True or (board[:,1] == win2).all() == True or (board[:,2] == win2).all() == True:
                    print("You have lost. Better luck next time!")
                    win == True
                    break
                if board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
                    print("You have lost. Better luck next time!")
                    win == True
                    break
                if board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
                    print("You have lost. Better luck next time!")
                    win == True
                    break
            ## ask to play again
            while correctagain == False:    
                again = input("Would you like to play again? (Y/N)")
                again = again.strip()
                if again not in yes and again not in no:
                    print("Invalid selection. Please choose 'Yes' or 'No'.")
                    continue
                if again in no:
                    replay = False
                    correctagain = True
                    firstchoice = True
                    break
                break
                if again in yes:
                    win = False
                    break
    if first in no:
        while replay == True:
            board = np.array([  
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            ])
            while win == False:
                print("Here is my move...")
                time.sleep(1)
                goodcompmove = False
                while goodcompmove == False:
                    comprow = random.choice(array)
                    compcol = random.choice(array)
                    if board[comprow][compcol] != 0:
                        continue
                    else:
                        board[int(comprow)][int(compcol)] = 2
                        print(board)
                        time.sleep(1)
                        goodcompmove = True
                ##checking for a computer win or a stalemate
                if (board[0] == win2).all() == True or (board[1] == win2).all() == True or (board[2] == win2).all() == True:
                    print("You have lost. Better luck next time!")
                    win == True
                    break
                if (board[:,0] == win2).all() == True or (board[:,1] == win2).all() == True or (board[:,2] == win2).all() == True:
                    print("You have lost. Better luck next time!")
                    win == True
                    break
                if board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
                    print("You have lost. Better luck next time!")
                    win == True
                    break
                if board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
                    print("You have lost. Better luck next time!")
                    win == True
                    break
                if (board == compareboard).any() == False:
                    print("We have reached a stalemate! There is no winner!")
                    win == True
                    break
                nextmove = str(input("Your turn: "))
                try:
                    int(nextmove[0])
                except:
                    print("Whoops! Please enter a valid move!")
                    continue
                try:
                    int(nextmove[1])
                except:
                    print("Whoops! Please enter a valid move!")
                    continue
                if int(nextmove[0]) not in array or int(nextmove[1]) not in array:
                    print("Please select a valid row and column! Try again...")
                    time.sleep(1)
                    continue
                elif board[int(nextmove[0])][int(nextmove[1])] != 0:
                    print("That spot is already taken! Please select again!")
                    time.sleep(1)
                    continue
                board[int(nextmove[0])][int(nextmove[1])] = 1
                print(board)
                time.sleep(1)
                if (board[0] == win1).all() == True or (board[1] == win1).all() == True or (board[2] == win1).all() == True: ##row win
                    print("You have won! Congratulations!")
                    win == True
                    break
                if (board[:,0] == win1).all() == True or (board[:,1] == win1).all() == True or (board[:,2] == win1).all() == True: ##col win
                    print("You have won! Congratulations!")
                    win == True
                    break
                if board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1: ##diag win
                    print("You have won! Congratulations!")
                    win == True
                    break
                if board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1: ##diag win
                    print("You have won! Congratulations!")
                    win == True
                    break
            while correctagain == False:    
                again = input("Would you like to play again? (Y/N)")
                again = again.strip()
                if again not in yes and again not in no:
                    print("Invalid selection. Please choose 'Yes' or 'No'.")
                    continue
                if again in no:
                    replay = False
                    correctagain = True
                    firstchoice = True
                    break
                break
                if again in yes:
                    win = False
                    break

sys.exit()
