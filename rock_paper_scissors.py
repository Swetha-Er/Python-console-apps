import random

choice = ("rock", "paper", "scissors")
playing = True

while playing:
    player = None
    while player not in choice:
        player = input(f"enter one from {choice}: ")
        computer = random.choice(choice)

    if player == computer:
        print("It's a Tie!")
    elif player == "rock" and computer == "scissors":
        print("You Won!")
    elif player == "paper" and computer == "rock":
        print("You Won!")
    elif player == "scissors" and computer == "scissors":
        print("You Won!")
    else:
        print("You Lose!🥲")
    if not input("Do you want to play again(y/n): ").lower() == 'y':
         playing = False   