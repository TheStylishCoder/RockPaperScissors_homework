from flask import render_template, redirect
from app import app
from app.models.player import Player
from app.models.game import Game

@app.route('/')
def index():
    return render_template('base.html', title='RockPaperScissors')

# @app.route('/', methods=['POST'])
# def play():

@app.route('/welcome')
def welcome_page():
    return render_template('rules.html', title = 'RockPaperScissors')

@app.route('/<player_1_choice>/<player_2_choice>')
def play(player_1_choice, player_2_choice):
    player_1 = Player("Player 1", player_1_choice)
    player_2 = Player("Player 2", player_2_choice)
    game = Game()
    result = game.determine_winner(player_1, player_2)
    print(result)
    
    
    return render_template('index.html', title='RockPaperScissors', player1=player_1, player2=player_2, result=result)