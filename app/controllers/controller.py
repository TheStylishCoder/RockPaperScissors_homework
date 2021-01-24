from flask import render_template, redirect, request
from app import app
from app.models.player import Player
from app.models.game import Game

@app.route('/')
def index():
    return render_template('index.html', title='RockPaperScissors')

@app.route('/play')
def play_page():
    return render_template('play.html', title='RockPaperScissors')

@app.route('/play', methods=['POST'])
def add_player():
    name = request.form['name']
    choice = request.form['choice']
    newplayer = Player(name=name, choice=choice)
    game = Game()
    choices = ["rock", "paper", "scissors"]
    computer_choice = game.make_choice(choices)
    computer = Player("The Computer", computer_choice)
    result = game.determine_winner(newplayer, computer)
    print(result)
    
    return render_template('result.html', title = 'RockPaperScissors', player1=newplayer, player2=computer, result=result)
  
@app.route('/play2')
def players_page():
    return render_template('play2.html', title='RockPaperScissors')

@app.route('/play2', methods=['POST'])
def add_players():
    name1 = request.form['name1']
    choice1 = request.form['choice1']
    player_1 = Player(name=name1, choice=choice1)
    name2 = request.form['name2']
    choice2 = request.form['choice2']
    player_2 = Player(name=name2, choice=choice2)
    game = Game()
    result = game.determine_winner(player_1, player_2)
    print(result)
    
    return render_template('result.html', title = 'RockPaperScissors', player1=player_1, player2=player_2, result=result)
  


@app.route('/play/result')
def results():
    return render_template('result.html', title= 'RockPaperScissors')

@app.route('/rules')
def welcome_page():
    return render_template('rules.html', title = 'RockPaperScissors')

@app.route('/<player_1_choice>/<player_2_choice>')
def play(player_1_choice, player_2_choice):
    player_1 = Player("Player 1", player_1_choice)
    player_2 = Player("Player 2", player_2_choice)
    game = Game()
    result = game.determine_winner(player_1, player_2)
    print(result)
    
    
    return render_template('result.html', title='RockPaperScissors', player1=player_1, player2=player_2, result=result)