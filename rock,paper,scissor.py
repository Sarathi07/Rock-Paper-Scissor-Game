#rock,paper,scissor game developed by Sarathi using python
import random
choices = ["Rock", "Paper", "Scissors"]
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or Scissors or End?").capitalize()
    random.shuffle(choices)
    computer=choices[0]
    print(f"Computer Choice is {computer}")
## Conditions of Rock,Paper and Scissors
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu_score+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpu_score+=1
        else:
            print("You win!", player, "covers", computer)
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose…", computer, "smashes", player)
            cpu_score+=1
        else:
            print("You win!", player, "cut", computer)
            player_score+=1
    elif player=="End":
        print("Final Scores:")
        print(f"Computer Score:{cpu_score}")
        print(f"Player Score:{player_score}")
        break
