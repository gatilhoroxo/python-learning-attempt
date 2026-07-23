import random 

print("Rock, Scissors, Paper")

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    # list
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    # dictionary
    choices = {"player_choice": player_choice, "computer_choice": computer_choice}
    return choices

def check_win(player, computer):
    print("You chose " + player + ", computer chose " + computer)
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "paper":
            return "Paper covers rock! You lose."
        else:
            return "Rock smashes scissors! You won!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! YOU WON!"
        else:
            return "Scissors cuts paper! You lose."
    else:
        if computer == "rock":
            return "Rock smashes scissors! YOU LOSE. "
        else:
            return "Scissors cuts paper! YOU WON! "

#main code

choices = get_choices()

message = check_win(choices["player_choice"], choices["computer_choice"])

print(message)

