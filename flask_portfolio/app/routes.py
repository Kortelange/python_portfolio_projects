from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session, make_response
from morse_code import text_to_morse
from tictactoe import TicTacToe

# Define blueprints
main = Blueprint('main', __name__)
morse_code = Blueprint('morse_code', __name__)
tic_tac_toe = Blueprint('tic_tac_toe', __name__)

@main.route("/")
def home():
    return render_template('index.html')


@morse_code.route("/")
def home():
    text_to_translate='Hello Stranger!'
    return render_template(
        'morse_code.html',
        text_to_translate=text_to_translate,
        translation=text_to_morse(text_to_translate)
        )


@morse_code.route("/translate_to_morse", methods=['POST'])
def translate_to_morse():
    if request.method == "POST":
        text_to_translate = request.form['text_to_translate']
        translation = text_to_morse(text_to_translate)
        return render_template(
            'morse_code.html', 
            text_to_translate=text_to_translate, 
            translation=translation
            )
    return redirect(url_for('morse_code.home'))


@tic_tac_toe.route("/")
def home():
    return render_template(
        'tictactoe.html', 
        game_started=False
    )


@tic_tac_toe.route("/start_game", methods=['POST'])
def start_game():
    player = request.json['player'].lower()
    game = TicTacToe()
    session['player_x'] = game.player_x
    session['player_o'] = game.player_o
    return jsonify(player=player)


def change_player(player):
    return 'x' if player == 'o' else 'o'


def update_game_session(game: TicTacToe):
    session['player_x'] = game.player_x
    session['player_o'] = game.player_o


def get_game_from_session() -> TicTacToe:
    return TicTacToe(session['player_x'], session['player_o'])


@tic_tac_toe.route("/place", methods=['POST'])
def place():
    player = request.json['player']
    index = int(request.json['index'])
    game = get_game_from_session()
    try:
        game.place(player, index)
        game_over = game.check_win(player)
        player = change_player(player)
        update_game_session(game)
        return jsonify(
            player=player,
            available_spots=list(game.get_avaliable_slots()),
            game_over=game_over
        )
    except:
        return jsonify(error="Please place at an unoccupied slot."), 400
