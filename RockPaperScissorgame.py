import random
#define options
options=["rock","paper","scissor"]
#define a function to determine winner
def determine_winner(player_choice,computer_choice, player_name):
    if player_choice==computer_choice:
        return "tie"
    elif player_choice=="rock" and computer_choice=="paper":
        return player_name
    elif player_choice=="paper" and computer_choice=="rock":
        return player_name
    elif player_choice=="scissor" and computer_choice=="paper":
        return player_name
    else:
        return "computer"
#loop until the player decides to quit
player_name=input("Enter your name:")
while True:
    #ask player to choose rock or paper or scissor
    
    player_choice=input("choose rock or paper or scissor or else(choose q to quit):").lower()
    if player_choice=="q":
        break
    if player_choice not in options:
        print("Invalid Choice")
        continue
    computer_choice=random.choice(options)
    winner=determine_winner(player_choice, computer_choice, player_name)
    print(player_name + " choose", player_choice +".The computer choose", computer_choice +".")
    if winner=="tie":
        print("It's a tie!")
    else:
        print(winner.capitalize()+" wins!")

