import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']

    def get_player_choice(self):
        while True:
            player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
            if player_choice in self.choices:
                return player_choice
            else:
                print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            return "You win!"
        else:
            return "Computer wins!"

    def play_game(self):
        print("Let's play Rock, Paper, Scissors!")
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        print(self.determine_winner(player_choice, computer_choice))

#
game = RockPaperScissors()
game.play_game()
