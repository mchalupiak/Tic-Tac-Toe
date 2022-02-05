from GameStart import startboard
from GameBoard import gameboard
from AiTurn import aigo
from time import sleep

def hasWinner():
    for i in range(len(winningMoves)):
        if gameSpaces[winningMoves[i][0]] == gameSpaces[winningMoves[i][1]] == gameSpaces[winningMoves[i][2]] and " " not in [gameSpaces[winningMoves[i][0]], gameSpaces[winningMoves[i][1]], gameSpaces[winningMoves[i][2]]]:
            return True
    return False

incorrectPiece = 0
on = True
startboard() ; sleep(.5)
gameSpaces = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
winningMoves = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [3, 5, 8], [0, 4, 8], [2, 4, 6]]
while on:
    userPiece = input("Now, what piece do you want to be, X or O? ")
    if incorrectPiece > 5:
        print("Fine, you can be than piece")
        break
    
    if userPiece.upper() in ["X", "O"]:
        print("You will be " + userPiece.upper())
        break
       
    else:
        print("Sorry, you didn't pick X or O! (O, not Zero)")
        incorrectPiece += 1

if userPiece.upper() == "X":
    aiPiece = "O"

elif userPiece.upper() == "O":
    aiPiece = "X"

while on:
    
    userMove = input("What spot do you want to place a piece on? Ex: 1, 2, 3, etc ")
    if gameSpaces[int(userMove)-1] == " ":
        gameSpaces[int(userMove) - 1] = userPiece.upper()
        if hasWinner():
            gameboard(gameSpaces[0], gameSpaces[1], gameSpaces[2], gameSpaces[3], gameSpaces[4], gameSpaces[5], gameSpaces[6], gameSpaces[7], gameSpaces[8])
            print("You won!")
            break
    
    else:
        print("Sorry, that space is already taken")
        continue
    
    computerMove = aigo(gameSpaces)
    if computerMove != 9:
        gameSpaces[computerMove] = aiPiece
        if hasWinner():
            gameboard(gameSpaces[0], gameSpaces[1], gameSpaces[2], gameSpaces[3], gameSpaces[4], gameSpaces[5], gameSpaces[6], gameSpaces[7], gameSpaces[8])
            print("You lost!")
            break
    else:
        print("Board full... Game is over")
        on = False
    gameboard(gameSpaces[0], gameSpaces[1], gameSpaces[2], gameSpaces[3], gameSpaces[4], gameSpaces[5], gameSpaces[6], gameSpaces[7], gameSpaces[8])

