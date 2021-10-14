print("......Rock......")
print("......Paper......")
print("......Scissors......")

player1 = input("Player 1, play your move ")
player2 = input("Player 2, play your move ")

# Logic for the rock 
if player1 == "rock" and player2 == "scissors" :
    print("Player 1 wins")
elif player1  == "rock" and player2 == "paper":
    print("Player 2 wins")
# Logic for the paper
elif player1 == "paper" and player2 == "scissors" :
    print("Player 2 wins")
elif player1  == "paper" and player2 == "rock":
    print("Player 1 wins")
# Logic for the scissors
elif player1 == "scissors" and player2 == "rock" :
    print("Player 2 wins")
elif player1  == "scissors" and player2 == "paper":
    print("Player 1 wins")
# If both player1 and player 2 are equal
elif player1 == player2:
    print("A DRAW")
else:
    print("Oops cannot read")