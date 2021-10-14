import random
print("......Rock......")
print("......Paper......")
print("......Scissors......")

rand_num  = random.randint(0, 2)

if  rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
elif rand_num == 2:
    computer = "scissors"


player = input("Player, play your move: ")
print("The computer played: ", computer)

if player == computer: 
    print("A Tie")
# Logic for rock
elif player == "rock" :
    if computer == "scissors":
        print("Player wins")
    elif computer == "paper": 
        print("Computer wins")
# Logic for the paper
elif player == "paper" :
    if computer == "rock": 
        print("Player wins")
    elif computer == "scissors":
        print("Computer wins")
# Logic for scissors
elif player == "paper" :
    if computer == "rock": 
        print("Player wins")
    elif computer == "scissors":
        print("Computer wins")

else: 
    print("Meh i don't get it")
