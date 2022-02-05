import random as rd

def aigo(list):
    moves = []
    while 1 == 1:
        computerMove = rd.randint(0,8)
        if list[computerMove] == " ":
            break

        else:
            if computerMove not in moves:
                moves.append(computerMove)
            if len(moves) >= 9:
                return 9
            continue

    return computerMove
