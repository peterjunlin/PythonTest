from random import randint


def play_game():
    value_names = ["rock", "paper", "scissors"]

    # computer's hand
    computer = randint(0, 2)

    # user's hand
    s = input("0-rock, 1-paper, 2-scissors")
    if s.isnumeric():
        player = int(s)
    else:
        print("Input is not valid.")
        return;

    # who won
    if computer == player:
        print("tie")
    elif (computer == 0 and player == 1) \
            or (computer == 1 and player == 2)\
            or (computer == 2 and player == 0):
        print("Player won.", value_names[computer], value_names[player])
    else:
        print("Computer won.", value_names[computer], value_names[player])


if __name__ == '__main__':
    play_game()
