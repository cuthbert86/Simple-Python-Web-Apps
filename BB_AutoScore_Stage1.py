import time
# from datetime import datetime
# import math


P1Score = int(0)
P2Score = int(0)


start_time = time.time()
duration = 100

P1_name = str(input("Enter Player 1 Name: "))
P2_name = str(input("Enter Player 2 Name: "))


def P1Turn(P1Score):
    Break = int(0)
    print(f"{P1_name} turn")
    print(f"What did {P1_name} Score?")
    Break = int(input())

    if Break == 1:
        P1Score = 0     # Black mushroom

    else:
        P1Score = P1Score + Break

    print(f"Current {P1_name} score = {P1Score}")
    return P1Score


def P2Turn(P2Score):
    Break = int(0)
    print(f"{P2_name} turn")
    print(f"What did {P2_name} Score?")
    Break = int(input())
    if Break == 1:
        P2Score = 0     # Black Mushroom 

    else:
        P2Score = P2Score + Break

    print(f"Current {P2_name} score = {P2Score}")
    return P2Score


while (time.time() - start_time) < duration:
    print(P1Score)
    P1Score = P1Turn(P1Score)
    print(P2Score)
    P2Score = P2Turn(P1Score)

else:
    if P1Score > P2Score:
        print(f"{P1_name} is the winner!")
        print(f"{P1_name} score : {P1Score}")
        print(f"Looser {P2_name} score : {P2Score}")
    elif P2Score > P1Score:
        print(f"{P2_name} is the winner!")
        print(f"{P2_name} score : {P2Score}")
        print(f"Looser {P1_name} score : {P1Score}")
    else:
        print(f"{P1_name} and {P2_name} have drawn the game")
        print(f"Both loosers scored {P1Score}")


print("End of program")
