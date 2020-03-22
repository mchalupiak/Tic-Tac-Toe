import random as rd

def aigo(list):
    while 1 == 1:
        computerMove = rd.randint(0,8)
        if list[computerMove] == " ":
            break

        else:
            continue

    return computerMove
