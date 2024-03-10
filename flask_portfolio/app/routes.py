from flask import Blueprint, render_template, request, redirect, url_for
from morse_code import text_to_morse

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
    return render_template('tictactoe.html')
