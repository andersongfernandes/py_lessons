# time code 03:10:27
# random

import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock, paper or scissors? ").lower()

    if player == computer:
        print("Computer = "+computer)
        print("Player = "+player)
        print("Tie!")
        
    elif player == "rock":
        if computer == "paper":
            print("Computer = "+computer)
            print("Player = "+player)
            print("Computer wins!")
        else:
            print("Computer = "+computer)
            print("Player = "+player)
            print("You win!")

    elif player == "paper":
        if computer == "scissors":
            print("Computer = "+computer)
            print("Player = "+player)
            print("Computer wins!")
        else:
            print("Computer = "+computer)
            print("Player = "+player)
            print("You win!")

    else:
        if computer == "rock":
            print("Computer = "+computer)
            print("Player = "+player)
            print("Computer wins!")
        else:
            print("Computer = "+computer)
            print("Player = "+player)
            print("You win!")
    
    play_again = None
    player_answers = ["y", "n"]
    while play_again not in player_answers:
        play_again = input("Play again? (Y/N): ").lower()

    if play_again == "n":
        break

print("It was wonderful! Bye!!")
    