# I want to create a game of rock paper scissors, the winner of the game is determined by three simple rules:
# 1. Rock beats scissors.
# 2. Scissors beat paper.
# 3. Paper beats rock.
# 
# Make the game multiplayer, where the computer will be player's opponent and can randomly choose one of the
# elements (rock, paper, or scissors) for each move, just like the player. Player's interaction in the game
# will be through the console (Terminal).
# 
# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

import random

def rock_paper_scissors():
    player_score = 0
    computer_score = 0
    options = ['rock', 'paper', 'scissors']

    while True:
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        computer_choice = random.choice(options)

        if player_choice not in options:
            print("Invalid option, please choose rock, paper, or scissors.")
            continue

        if player_choice == computer_choice:
            print(f"Player: {player_choice}, Computer: {computer_choice}. It's a tie!")
        elif player_choice == 'rock' and computer_choice == 'scissors':
            player_score += 1
            print(f"Player: {player_choice}, Computer: {computer_choice}. Player wins!")
        elif player_choice == 'scissors' and computer_choice == 'paper':
            player_score += 1
            print(f"Player: {player_choice}, Computer: {computer_choice}. Player wins!")
        elif player_choice == 'paper' and computer_choice == 'rock':
            player_score += 1
            print(f"Player: {player_choice}, Computer: {computer_choice}. Player wins!")
        else:
            computer_score += 1
            print(f"Player: {player_choice}, Computer: {computer_choice}. Computer wins!")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print(f"Player: {player_score}, Computer: {computer_score}")
            break

rock_paper_scissors()

# To run the game, type the following command in the Terminal:
# python3 app.py
#
# The game will start and you can play by typing rock, paper, or scissors. The game will inform you if you won, lost, or tied with the computer.
# At the end of each round, you can choose whether to play again. The game will display the player's score at the end of the game.
# Enjoy playing!
