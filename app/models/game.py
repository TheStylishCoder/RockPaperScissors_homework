class Game():
    

    def determine_winner(self, player_1, player_2):
        if player_1.choice == "paper" and player_2.choice == "rock":
            return "player 1 wins"
        elif player_1.choice == "paper" and player_2.choice == "scissors":
            return "player 2 wins"
        elif player_1.choice == "rock" and player_2.choice == "paper":
            return "player 2 wins"
        elif player_1.choice == "rock" and player_2.choice == "scissors":
            return "player 1 wins"
        elif player_1.choice == "scissors" and player_2.choice == "paper":
            return "player 1 won"
        elif player_1.choice == "scissors" and player_2.choice == "rock":
            return "player 2 has won"
        else:
            return None 
