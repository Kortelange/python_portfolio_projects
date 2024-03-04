from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template('index.html')


morse_code = Blueprint('morse_code', __name__)

@morse_code.route("/")
def home():
    return render_template('morse_code.html')
