# Rock Paper Scissors

def main():
    player1 = input("Player 1, enter your choice (R/P/S): ")
    player2 = input("Player 2, enter your choice (R/P/S): ")


    if player1 == "P" and player2 == "S":
        print("Player 2 won!")

    elif player1 == "S" and player2 == "P":
        print("Player 1 won!")

    elif player1 == "P" and player2 == "R":
        print("Player 1 won!")

    elif player1 == "R" and player2 == "P":
        print("Player 2 won!")

    elif player1 == "R" and player2 == "S":
        print("Player 1 won!")

    elif player1 == "S" and player2 == "R":
        print("Player 2 won!")

    else:
        print("It's a tie!")


if __name__ == "__main__":
    main()
