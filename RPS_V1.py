print("......Rock......")
print("......Paper......")
print("......Scissors......")

player1 = input("Player 1, play your move ")
player2 = input("Player 2, play your move ")

# Tie breaker
if player1 == player2: 
    print("A Tie")
# Logic for rock
elif player1 == "rock" :
    if player2 == "scissors":
        print("Player 1 wins")
    elif player2 == "paper": 
        print("Player 2 wins")
# Logic for the paper
elif player1 == "paper" :
    if player2 == "rock": 
        print("Player 1 wins")
    elif player2 == "scissors":
        print("Player 2 wins")
# Logic for scissors
elif player1 == "paper" :
    if player2 == "rock": 
        print("Player 1 wins")
    elif player2 == "scissors":
        print("Player 2 wins")

else: 
    print("Meh i don't get it")