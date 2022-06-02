#import random
import random
game = ["random","paper","scissors"]
cpu = random.choice(game)
player = None

while player not in game:
    player = input("rock, paper. or scissors?:\n".lower())
if player == cpu:
    print ("computer:", cpu, "Player", player)
    print("Tie")
elif player == "rock":
    if cpu == "paper":
        print("computer:",cpu, "player:", player)
        print("You Loose")
    if cpu == "scissors":
        print("computer:",cpu, "player:", player)
        print("You Win")
elif player == "scissors":
    if cpu == "rock":
        print("computer:",cpu, "player:", player)
        print("You Loose")
    if cpu == "paper":
        print("computer:",cpu, "player:", player)
        print("You Win")
elif player == "paper":
    if cpu == "scissors":
        print("computer:",cpu, "player:", player)
        print("You Loose")
    if cpu == "rock":
        print("computer:",cpu, "player:", player)
        print("You Win")