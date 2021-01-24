import random 

class Game():
    

    def determine_winner(self, player_1, player_2):
        if (player_1.choice.lower()) == "paper" and (player_2.choice.lower()) == "rock":
            return "Player 1 wins"
        elif (player_1.choice.lower()) == "paper" and (player_2.choice.lower()) == "scissors":
            return "Player 2 wins"
        elif (player_1.choice.lower()) == "rock" and (player_2.choice.lower()) == "paper":
            return "Player 2 wins"
        elif (player_1.choice.lower()) == "rock" and (player_2.choice.lower()) == "scissors":
            return "Player 1 wins"
        elif (player_1.choice.lower()) == "scissors" and (player_2.choice.lower()) == "paper":
            return "Player 1 won"
        elif (player_1.choice.lower()) == "scissors" and (player_2.choice.lower()) == "rock":
            return "Player 2 has won"
        else:
            return None 


    
    def make_choice(self, choices):
        return random.choice(choices)

