from GameStart import startboard
from GameBoard import gameboard
from AiTurn import aigo
from time import sleep

incorrectPiece = 0
on = True
startboard() ; sleep(.5)
gameSpaces = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
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
    
    else:
        print("Sorry, that space is already taken")
        continue
    
    gameSpaces[aigo(gameSpaces)] = aiPiece
    gameboard(gameSpaces[0], gameSpaces[1], gameSpaces[2], gameSpaces[3], gameSpaces[4], gameSpaces[5], gameSpaces[6], gameSpaces[7], gameSpaces[8])
    